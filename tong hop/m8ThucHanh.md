# Practice Exercises for Module 8: GANs for Cyber Security

## Part 1: Understanding GANs Fundamentals

### Exercise 1.1: Conceptual Understanding (Beginner)
**Objective:** Test your grasp of GAN basics

**Questions:**
1. In your own words, explain the adversarial relationship between Generator and Discriminator using a non-technical analogy (not counterfeiter/detective).

2. Fill in the blanks:
   - The Generator tries to _________ the Discriminator
   - The Discriminator tries to _________ between real and fake data
   - As training progresses, both networks become _________

3. Draw a simple flowchart showing how data flows through a GAN during training.

**Answer Key:**
1. Example: Artist (G) vs Art Critic (D), Student (G) vs Teacher (D), etc.
2. fool, distinguish, better/more skilled
3. Should show: Noise → Generator → Fake Data → Discriminator → Real/Fake Decision

### Exercise 1.2: Mathematical Foundation (Intermediate)
**Objective:** Apply GAN loss function concepts

**Problem:** Given the GAN objective function:
```
min_G max_D V(D,G) = E[log D(x)] + E[log(1-D(G(z)))]
```

1. What happens to the loss when:
   - D(x) = 1 (discriminator correctly identifies real data)?
   - D(G(z)) = 0 (discriminator correctly identifies fake data)?
   - D(G(z)) = 1 (generator successfully fools discriminator)?

2. Why is this a minimax problem?

### Exercise 1.3: Coding Challenge (Intermediate)
**Objective:** Implement basic GAN structure

```python
# Complete the missing parts of this GAN implementation
import torch
import torch.nn as nn

class SimpleGenerator(nn.Module):
    def __init__(self, noise_dim, output_dim):
        super(SimpleGenerator, self).__init__()
        # TODO: Define a 3-layer neural network
        # Layer 1: noise_dim → 128, ReLU activation
        # Layer 2: 128 → 256, ReLU activation  
        # Layer 3: 256 → output_dim, Tanh activation
        self.model = nn.Sequential(
            # YOUR CODE HERE
        )
    
    def forward(self, x):
        # YOUR CODE HERE
        pass

class SimpleDiscriminator(nn.Module):
    def __init__(self, input_dim):
        super(SimpleDiscriminator, self).__init__()
        # TODO: Define a 3-layer neural network
        # Layer 1: input_dim → 256, ReLU activation
        # Layer 2: 256 → 128, ReLU activation
        # Layer 3: 128 → 1, Sigmoid activation
        self.model = nn.Sequential(
            # YOUR CODE HERE
        )
    
    def forward(self, x):
        # YOUR CODE HERE
        pass

# Test your implementation
noise_dim = 100
data_dim = 784  # For MNIST-like data
generator = SimpleGenerator(noise_dim, data_dim)
discriminator = SimpleDiscriminator(data_dim)

# Generate test data
test_noise = torch.randn(32, noise_dim)
fake_data = generator(test_noise)
prediction = discriminator(fake_data)

print(f"Generated data shape: {fake_data.shape}")
print(f"Discriminator output shape: {prediction.shape}")
```

## Part 2: Python Libraries for GANs

### Exercise 2.1: Library Setup Challenge (Beginner)
**Objective:** Set up proper GAN development environment

**Task:** Create a Python script that:
1. Imports all necessary libraries for GAN development
2. Checks if GPU is available for PyTorch/TensorFlow
3. Sets up proper random seeds for reproducibility
4. Creates a simple data loader for a small dataset

```python
# Complete this setup script
import torch
# TODO: Add other necessary imports

def setup_environment():
    # TODO: Check for GPU availability
    # TODO: Set random seeds for reproducibility
    # TODO: Print system information
    pass

def create_dataloader(data, batch_size=32):
    # TODO: Create a DataLoader for training
    pass

if __name__ == "__main__":
    setup_environment()
```

### Exercise 2.2: Data Preprocessing Pipeline (Intermediate)
**Objective:** Build data pipeline for GAN training

**Task:** Create a preprocessing pipeline for network traffic data:
```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Sample network traffic data structure
def create_network_data_pipeline():
    """
    Create a pipeline that:
    1. Loads network traffic data
    2. Handles missing values
    3. Encodes categorical features
    4. Normalizes numerical features
    5. Splits into features suitable for GAN training
    """
    # TODO: Implement the pipeline
    pass

# Test data (you create this)
sample_data = {
    'src_ip': ['192.168.1.1', '10.0.0.1', '172.16.0.1'],
    'dst_port': [80, 443, 22],
    'protocol': ['TCP', 'UDP', 'TCP'],
    'packet_size': [1500, 500, 64],
    'duration': [0.1, 2.5, 0.01],
    'label': ['normal', 'attack', 'normal']
}

# Process the data
processed_data = create_network_data_pipeline()
```

## Part 3: Network Attack via Model Substitution

### Exercise 3.1: Query Pattern Analysis (Intermediate)
**Objective:** Understand how attackers probe target models

**Scenario:** You're a red team member testing a company's image classification API used for document verification.

**Task:**
```python
# Simulate the reconnaissance phase of a substitution attack
import requests
import json
from PIL import Image
import numpy as np

class ModelProbing:
    def __init__(self, target_api_url):
        self.api_url = target_api_url
        self.query_log = []
    
    def probe_model(self, test_images):
        """
        TODO: Implement probing strategy
        1. Send different types of images to the API
        2. Record input-output pairs
        3. Analyze response patterns
        4. Identify decision boundaries
        """
        pass
    
    def analyze_responses(self):
        """
        TODO: Analyze collected responses to understand model behavior
        """
        pass

# Questions to answer:
# 1. What types of queries would be most informative for building a substitute?
# 2. How would you avoid detection while probing?
# 3. What patterns in responses would indicate model architecture?
```

### Exercise 3.2: Substitute Model Training (Advanced)
**Objective:** Build a substitute model from query data

```python
class SubstituteModel:
    def __init__(self):
        self.model = None
        self.training_data = []
    
    def collect_training_data(self, queries, responses):
        """
        TODO: Process query-response pairs for training
        """
        pass
    
    def train_substitute(self):
        """
        TODO: Train a model that mimics target behavior
        """
        pass
    
    def generate_adversarial_examples(self, legitimate_inputs):
        """
        TODO: Use substitute model to create adversarial examples
        """
        pass

# Practical Challenge:
# Given 1000 query-response pairs from a spam detection API,
# build a substitute model and generate emails that evade detection
```

### Exercise 3.3: Defense Implementation (Advanced)
**Objective:** Implement defenses against model substitution

```python
class SubstitutionDefense:
    def __init__(self):
        self.query_monitor = QueryMonitor()
        self.response_randomizer = ResponseRandomizer()
    
    def detect_probing(self, user_queries):
        """
        TODO: Implement detection of suspicious query patterns
        - High query volume from single source
        - Systematic exploration of input space  
        - Queries designed to map decision boundaries
        """
        pass
    
    def add_defensive_noise(self, model_output):
        """
        TODO: Add controlled randomness to outputs
        """
        pass

# Challenge: Design a complete defense system
# that maintains API usability while preventing substitution attacks
```

## Part 4: IDS Evasion via GAN

### Exercise 4.1: Network Traffic Analysis (Intermediate)
**Objective:** Understand normal vs. malicious traffic patterns

**Task:** Analyze the KDD Cup dataset for IDS training:
```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def analyze_traffic_patterns():
    """
    TODO: Load KDD Cup or similar network intrusion dataset
    1. Identify key features that distinguish attack traffic
    2. Train a simple IDS classifier  
    3. Analyze which features are most important for detection
    4. Identify potential evasion opportunities
    """
    pass

# Questions:
# 1. Which traffic features are hardest for attackers to modify?
# 2. What attack types are easiest to disguise as normal traffic?
# 3. How would you generate realistic-looking malicious traffic?
```

### Exercise 4.2: GAN-based Traffic Generation (Advanced)
**Objective:** Create GAN to generate evasive network traffic

```python
class TrafficGAN:
    def __init__(self, traffic_features=41):
        self.generator = self.build_generator(traffic_features)
        self.discriminator = self.build_discriminator(traffic_features)
        self.ids_model = None  # External IDS to evade
    
    def build_generator(self, output_dim):
        """
        TODO: Build generator for network traffic features
        Consider: packet size, duration, protocol, port numbers, etc.
        """
        pass
    
    def build_discriminator(self, input_dim):
        """
        TODO: Build discriminator for realistic traffic
        """
        pass
    
    def train_evasive_gan(self, normal_traffic, ids_model):
        """
        TODO: Train GAN with dual objectives:
        1. Generate realistic traffic (fool discriminator)
        2. Evade IDS detection (fool IDS model)
        """
        pass

# Challenge: Generate malicious traffic that:
# - Maintains malicious functionality
# - Appears normal to statistical analysis
# - Evades signature-based detection
```

### Exercise 4.3: IDS Hardening (Advanced)
**Objective:** Strengthen IDS against GAN-based evasion

```python
class RobustIDS:
    def __init__(self):
        self.ensemble_models = []
        self.anomaly_detector = None
        self.behavioral_analyzer = None
    
    def build_adversarial_robust_ids(self):
        """
        TODO: Create IDS resistant to GAN evasion:
        1. Ensemble of diverse detection methods
        2. Adversarial training with synthetic attacks
        3. Behavioral analysis beyond packet features
        4. Dynamic model updating
        """
        pass
    
    def detect_gan_generated_traffic(self, traffic_sample):
        """
        TODO: Identify artificially generated network traffic
        """
        pass

# Research Challenge:
# Design experiments to test IDS robustness against different GAN architectures
```

## Part 5: Facial Recognition Attacks with GANs

### Exercise 5.1: Face Morphing Implementation (Intermediate)
**Objective:** Create face morphing attacks

```python
import cv2
import numpy as np
from PIL import Image

class FaceMorphing:
    def __init__(self):
        self.face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    def extract_facial_landmarks(self, image):
        """
        TODO: Extract key facial points for morphing
        Use dlib or mediapipe for landmark detection
        """
        pass
    
    def morph_faces(self, face1, face2, alpha=0.5):
        """
        TODO: Create morphed face that combines features
        1. Align faces using landmarks
        2. Blend facial features
        3. Ensure realistic appearance
        """
        pass
    
    def test_against_face_recognition(self, morphed_face, target_system):
        """
        TODO: Test if morphed face fools recognition system
        """
        pass

# Practical Exercise:
# Create morphs of your face with celebrities and test against
# open-source face recognition systems (with consent!)
```

### Exercise 5.2: Deepfake Detection (Advanced)
**Objective:** Build defenses against face manipulation

```python
class DeepfakeDetector:
    def __init__(self):
        self.temporal_analyzer = None
        self.artifact_detector = None
        self.physiological_checker = None
    
    def detect_temporal_inconsistencies(self, video_frames):
        """
        TODO: Analyze frame-to-frame consistency
        - Facial landmark stability
        - Lighting consistency
        - Micro-expression authenticity
        """
        pass
    
    def detect_compression_artifacts(self, image):
        """
        TODO: Identify GAN-specific artifacts
        - Unusual compression patterns
        - Spectral analysis
        - Pixel-level inconsistencies
        """
        pass
    
    def physiological_validation(self, video):
        """
        TODO: Check for realistic human behavior
        - Blinking patterns
        - Pulse detection from face color changes
        - Natural head movements
        """
        pass

# Challenge: Build a comprehensive deepfake detector
# Test against various GAN architectures (StyleGAN, FaceSwap, etc.)
```

### Exercise 5.3: Adversarial Face Generation (Expert)
**Objective:** Create adversarial examples for face recognition

```python
class AdversarialFaceAttack:
    def __init__(self, target_model):
        self.target_model = target_model
        self.perturbation_generator = None
    
    def generate_adversarial_perturbation(self, face_image, target_identity):
        """
        TODO: Generate minimal perturbation to fool face recognition
        1. Use gradient-based attacks (FGSM, PGD)
        2. Ensure perturbations are imperceptible
        3. Maintain image realism
        """
        pass
    
    def physical_world_attack(self, face_image):
        """
        TODO: Generate perturbations that work in physical world
        - Account for lighting changes
        - Consider camera angle variations
        - Ensure printable/wearable modifications
        """
        pass
    
    def universal_adversarial_patch(self):
        """
        TODO: Create universal patch that fools face recognition
        regardless of underlying face
        """
        pass

# Advanced Challenge:
# Create adversarial glasses or makeup patterns that fool
# face recognition while looking natural to humans
```

## Comprehensive Integration Exercises

### Project 1: Red Team Exercise (Expert Level)
**Scenario:** You're hired to test a bank's AI-powered security systems

**Objective:** Design a comprehensive attack using multiple GAN techniques

```python
class BankSecurityTest:
    def __init__(self):
        self.target_systems = {
            'document_verification': None,
            'face_recognition': None,
            'fraud_detection': None,
            'network_ids': None
        }
    
    def reconnaissance_phase(self):
        """
        TODO: Gather intelligence on target systems
        - API endpoints and behavior
        - Security measures in place
        - Input/output formats
        """
        pass
    
    def multi_vector_attack(self):
        """
        TODO: Coordinate attacks across multiple systems:
        1. Use GAN to generate fake IDs for document verification
        2. Create deepfakes for video authentication
        3. Generate evasive network traffic for persistence
        4. Morph faces for physical access control bypass
        """
        pass
    
    def measure_attack_success(self):
        """
        TODO: Evaluate attack effectiveness and document findings
        """
        pass

# Deliverables:
# 1. Attack methodology document
# 2. Proof-of-concept implementations
# 3. Defense recommendations
# 4. Risk assessment report
```

### Project 2: Blue Team Defense (Expert Level)
**Scenario:** Design comprehensive GAN-aware security architecture

```python
class GANAwareSecuritySystem:
    def __init__(self):
        self.detection_layers = {}
        self.response_mechanisms = {}
        self.learning_systems = {}
    
    def design_layered_defense(self):
        """
        TODO: Create multi-layer defense against GAN attacks:
        1. Input validation and sanitization
        2. Real-time deepfake detection
        3. Behavioral analysis systems
        4. Anomaly detection for generated content
        5. Human-in-the-loop verification for high-risk cases
        """
        pass
    
    def adaptive_learning_system(self):
        """
        TODO: Implement system that learns from new attack types
        """
        pass
    
    def incident_response_automation(self):
        """
        TODO: Automated response to detected GAN attacks
        """
        pass

# Deliverables:
# 1. Security architecture diagram
# 2. Implementation prototypes
# 3. Testing methodology
# 4. Performance benchmarks
# 5. Cost-benefit analysis
```

## Assessment Rubric

### Beginner Exercises (Exercises 1.1, 2.1)
- **Understanding (40%):** Demonstrates grasp of basic GAN concepts
- **Implementation (40%):** Can set up environment and basic code structure
- **Critical Thinking (20%):** Identifies potential security implications

### Intermediate Exercises (Exercises 1.2, 1.3, 2.2, 3.1, 4.1, 5.1)
- **Technical Implementation (50%):** Working code with proper structure
- **Security Analysis (30%):** Identifies attack vectors and defenses
- **Innovation (20%):** Creative approaches to problems

### Advanced Exercises (Exercises 3.2, 3.3, 4.2, 4.3, 5.2, 5.3)
- **Technical Excellence (40%):** Sophisticated, working implementations
- **Security Expertise (35%):** Deep understanding of attack/defense dynamics
- **Research Quality (25%):** Novel insights and thorough analysis

### Expert Projects (Projects 1, 2)
- **Comprehensive Understanding (30%):** Integration of all module concepts
- **Professional Quality (30%):** Industry-ready implementations
- **Strategic Thinking (25%):** Long-term security implications
- **Communication (15%):** Clear documentation and presentation

## Bonus Challenges

1. **Implement a GAN that generates synthetic cybersecurity datasets** while preserving privacy
2. **Create a real-time deepfake detector** that can run on mobile devices
3. **Design a honeypot system** that uses GANs to generate convincing fake sensitive data
4. **Build a GAN-powered penetration testing tool** that generates realistic social engineering content

Remember: Always use these skills ethically and within legal boundaries. The goal is to strengthen cybersecurity, not to enable malicious activities!
