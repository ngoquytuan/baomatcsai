"""
TensorFlow GANs Demo - Module 8
Script đơn giản để demo GANs với MNIST dataset
"""

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt
import time

print("TensorFlow version:", tf.__version__)

# ============================================================
# 1. GENERATOR MODEL - Tạo ảnh giả từ noise
# ============================================================
def make_generator_model():
    """
    Generator: Chuyển đổi noise vector (100 chiều) thành ảnh 28x28
    """
    model = tf.keras.Sequential()

    # Input: 100 chiều noise
    model.add(layers.Dense(7*7*256, use_bias=False, input_shape=(100,)))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    # Reshape thành tensor 7x7x256
    model.add(layers.Reshape((7, 7, 256)))

    # Upsampling 1: 7x7x256 -> 7x7x128
    model.add(layers.Conv2DTranspose(128, (5, 5), strides=(1, 1),
                                     padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    # Upsampling 2: 7x7x128 -> 14x14x64
    model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2),
                                     padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    # Upsampling 3: 14x14x64 -> 28x28x1
    model.add(layers.Conv2DTranspose(1, (5, 5), strides=(2, 2),
                                     padding='same', use_bias=False,
                                     activation='tanh'))

    return model


# ============================================================
# 2. DISCRIMINATOR MODEL - Phân biệt ảnh thật/giả
# ============================================================
def make_discriminator_model():
    """
    Discriminator: Phân loại ảnh là thật (1) hay giả (0)
    """
    model = tf.keras.Sequential()

    # Input: ảnh 28x28x1
    model.add(layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same',
                           input_shape=[28, 28, 1]))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Flatten())
    model.add(layers.Dense(1))  # Output: 1 số (thật hay giả)

    return model


# ============================================================
# 3. LOSS FUNCTIONS
# ============================================================
cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)

def discriminator_loss(real_output, fake_output):
    """
    Loss của Discriminator:
    - Phạt khi phân loại sai ảnh thật
    - Phạt khi phân loại sai ảnh giả
    """
    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    total_loss = real_loss + fake_loss
    return total_loss

def generator_loss(fake_output):
    """
    Loss của Generator:
    - Generator muốn Discriminator phân loại ảnh giả là ảnh thật
    """
    return cross_entropy(tf.ones_like(fake_output), fake_output)


# ============================================================
# 4. OPTIMIZERS
# ============================================================
generator_optimizer = tf.keras.optimizers.Adam(1e-4)
discriminator_optimizer = tf.keras.optimizers.Adam(1e-4)


# ============================================================
# 5. TRAINING STEP
# ============================================================
@tf.function
def train_step(images, generator, discriminator):
    """
    Một bước training cho cả Generator và Discriminator
    """
    noise_dim = 100
    batch_size = images.shape[0]

    # Tạo random noise
    noise = tf.random.normal([batch_size, noise_dim])

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        # Generator tạo ảnh giả
        generated_images = generator(noise, training=True)

        # Discriminator đánh giá ảnh thật và giả
        real_output = discriminator(images, training=True)
        fake_output = discriminator(generated_images, training=True)

        # Tính loss
        gen_loss = generator_loss(fake_output)
        disc_loss = discriminator_loss(real_output, fake_output)

    # Tính gradients
    gradients_of_generator = gen_tape.gradient(gen_loss,
                                               generator.trainable_variables)
    gradients_of_discriminator = disc_tape.gradient(disc_loss,
                                                    discriminator.trainable_variables)

    # Cập nhật weights
    generator_optimizer.apply_gradients(zip(gradients_of_generator,
                                           generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator,
                                               discriminator.trainable_variables))

    return gen_loss, disc_loss


# ============================================================
# 6. GENERATE AND SAVE IMAGES
# ============================================================
def generate_and_save_images(model, epoch, test_input):
    """
    Tạo và hiển thị ảnh từ Generator
    """
    predictions = model(test_input, training=False)

    fig = plt.figure(figsize=(4, 4))

    for i in range(predictions.shape[0]):
        plt.subplot(4, 4, i+1)
        plt.imshow(predictions[i, :, :, 0] * 127.5 + 127.5, cmap='gray')
        plt.axis('off')

    plt.suptitle(f'Epoch {epoch}')
    plt.tight_layout()
    plt.savefig(f'lab8s/image_at_epoch_{epoch:04d}.png')
    print(f'Đã lưu ảnh: image_at_epoch_{epoch:04d}.png')
    plt.close()


# ============================================================
# 7. MAIN TRAINING FUNCTION
# ============================================================
def train_gan(dataset, epochs, generator, discriminator):
    """
    Training loop chính
    """
    noise_dim = 100
    num_examples_to_generate = 16

    # Tạo seed cố định để theo dõi quá trình học
    seed = tf.random.normal([num_examples_to_generate, noise_dim])

    for epoch in range(epochs):
        start = time.time()

        gen_loss_list = []
        disc_loss_list = []

        # Training qua từng batch
        for image_batch in dataset:
            gen_loss, disc_loss = train_step(image_batch, generator, discriminator)
            gen_loss_list.append(gen_loss)
            disc_loss_list.append(disc_loss)

        # Hiển thị progress
        avg_gen_loss = np.mean(gen_loss_list)
        avg_disc_loss = np.mean(disc_loss_list)

        print(f'Epoch {epoch + 1}/{epochs}')
        print(f'  Generator Loss: {avg_gen_loss:.4f}')
        print(f'  Discriminator Loss: {avg_disc_loss:.4f}')
        print(f'  Time: {time.time()-start:.2f} sec')

        # Tạo ảnh sau mỗi 5 epoch
        if (epoch + 1) % 5 == 0:
            generate_and_save_images(generator, epoch + 1, seed)

    # Tạo ảnh cuối cùng
    generate_and_save_images(generator, epochs, seed)
    print("\n✅ Training hoàn tất!")


# ============================================================
# 8. MAIN PROGRAM
# ============================================================
def main():
    print("="*60)
    print("DEMO: Generative Adversarial Networks (GANs)")
    print("Dataset: MNIST (Chữ số viết tay)")
    print("="*60)

    # Load MNIST dataset
    print("\n📥 Đang tải MNIST dataset...")
    (train_images, train_labels), (_, _) = tf.keras.datasets.mnist.load_data()

    # Preprocessing
    train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32')
    train_images = (train_images - 127.5) / 127.5  # Normalize về [-1, 1]

    BUFFER_SIZE = 60000
    BATCH_SIZE = 256

    # Tạo dataset
    train_dataset = tf.data.Dataset.from_tensor_slices(train_images)
    train_dataset = train_dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

    print(f"✅ Đã tải {len(train_images)} ảnh")
    print(f"📦 Batch size: {BATCH_SIZE}")

    # Tạo models
    print("\n🔨 Đang tạo Generator và Discriminator...")
    generator = make_generator_model()
    discriminator = make_discriminator_model()

    print("\n📊 Generator Model:")
    generator.summary()
    print("\n📊 Discriminator Model:")
    discriminator.summary()

    # Test generator với random noise
    print("\n🧪 Test Generator với random noise...")
    noise = tf.random.normal([1, 100])
    generated_image = generator(noise, training=False)
    print(f"Generated image shape: {generated_image.shape}")

    # Training
    EPOCHS = 20  # Số epoch đơn giản để demo nhanh
    print(f"\n🚀 Bắt đầu training {EPOCHS} epochs...")
    print("="*60)

    train_gan(train_dataset, EPOCHS, generator, discriminator)

    print("\n" + "="*60)
    print("🎉 DEMO HOÀN TẤT!")
    print("📁 Kiểm tra thư mục lab8s/ để xem các ảnh được tạo")
    print("="*60)


if __name__ == "__main__":
    main()
