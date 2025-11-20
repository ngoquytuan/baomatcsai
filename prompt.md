# LLM Prompt Template for Recreating ML Security Labs

Dưới đây là prompt chi tiết bạn có thể sử dụng để tái tạo lại các lab tương tự với LLM:

---

## 🎯 Master Prompt Template

```
I need you to create a complete, educational Python machine learning lab for cybersecurity students. 
The lab should follow these specific requirements:

## CORE REQUIREMENTS:

1. **Educational Purpose**: 
   - Design for students learning AI in cybersecurity
   - Clear learning objectives stated at the top
   - Progressive difficulty (basic → intermediate → advanced)
   - Include "aha!" moments where students discover patterns

2. **Code Architecture**:
   - Create 3 separate Python files:
     * `generate_[topic]_data.py` - Dataset generator
     * `verify_dataset.py` - Quick validation script
     * `lab[X]_[topic]_analysis.py` - Main analysis notebook
   
3. **Dataset Generator Requirements**:
   - Generate realistic, synthetic data
   - Include INTENTIONAL anomalies for detection
   - Use numpy random seed for reproducibility
   - Create clear "attacker" and "normal" patterns
   - Include detailed docstrings explaining the simulation
   - Print progress messages with emojis (📊, ✅, ⚠️, 🔍)

4. **Data Characteristics**:
   - Must demonstrate a SPECIFIC security scenario
   - Include timestamp/temporal elements
   - Have measurable features (numeric values)
   - Create obvious statistical differences between normal/anomalous behavior
   - Minimum 100-500 data points

5. **Verification Script**:
   - Quick check (< 5 seconds runtime)
   - Print summary statistics
   - Generate 1-3 visualization plots
   - Show clear visual evidence of anomalies
   - Save plots as PNG files

6. **Main Analysis Script**:
   - Implement 2-3 different ML algorithms
   - Use scikit-learn library
   - Include data preprocessing steps
   - Calculate performance metrics (accuracy, precision, recall, F1)
   - Generate comprehensive visualizations
   - Print detailed analysis results with explanations

7. **Code Style Requirements**:
   - Extensive comments explaining WHY, not just WHAT
   - Docstrings for all functions
   - Use descriptive variable names
   - Include "Student Exercise" sections
   - Add TODO comments for optional enhancements
   - Use print statements to guide students through execution

8. **Educational Features**:
   - Print section headers with === borders
   - Use emojis to highlight important outputs
   - Explain ML concepts in comments
   - Show intermediate results
   - Compare multiple approaches
   - Highlight security implications

9. **Visualization Requirements**:
   - Use matplotlib for plotting
   - Create subplots for comparisons
   - Use clear titles and labels
   - Include legends and grid lines
   - Save high-resolution images (dpi=200)
   - Use security-themed colors (red for threats, green for safe)

10. **Security Scenario**:
    - Based on REAL-WORLD attack patterns
    - Include both defender and attacker perspectives
    - Demonstrate practical detection methods
    - Show limitations of the approach

## SPECIFIC TOPIC:

Create a lab about: [INSERT YOUR TOPIC HERE]

Examples:
- "Keystroke dynamics for detecting shared account credentials"
- "Network traffic analysis for DDoS detection"
- "Email header analysis for phishing detection"
- "Mouse movement patterns for bot detection"
- "Login timing analysis for credential stuffing detection"

## SECURITY SCENARIO DETAILS:

- Normal behavior: [describe normal user behavior]
- Attack pattern: [describe malicious behavior]
- Detection goal: [what should ML identify]
- Features to analyze: [list 3-5 measurable features]

## ML ALGORITHMS TO USE:

1. [Algorithm 1] - for [reason]
2. [Algorithm 2] - for [comparison]
3. [Algorithm 3] - for [advanced detection]

## EXPECTED OUTPUT:

Provide complete, runnable Python code for all 3 files with:
- No placeholder code - everything must be functional
- Realistic data patterns
- Clear documentation
- Student-friendly explanations
- Professional formatting

## STYLE REFERENCE:

Use this style for comments:
```python
"""
Comprehensive Module Docstring
===============================
Explain the PURPOSE and CONTEXT
Include security scenario description
"""

def function_name(param):
    """
    Brief description
    
    Args:
        param: Explanation of parameter
    
    Returns:
        What the function returns
    
    Security Note:
        Why this is relevant for security analysis
    """
    # Explain the REASONING behind this step
    # Not just "calculate mean" but "calculate mean to establish baseline"
    code_here()
```

## DELIVERABLES:

1. Complete `generate_data.py` with realistic data generation
2. Complete `verify_dataset.py` with quick validation
3. Complete `lab_analysis.py` with ML implementation
4. Brief explanation of the security scenario
5. Instructions for students on how to run the lab

Make this lab engaging, educational, and professionally documented!
```

---

## 🔧 Ví dụ Prompt Cụ Thể

```
I need you to create a complete, educational Python machine learning lab for cybersecurity students 
following the master template above.

SPECIFIC TOPIC: Mouse movement pattern analysis for bot detection

SECURITY SCENARIO:
- Normal behavior: Human mouse movements with natural curves, pauses, and acceleration/deceleration
- Attack pattern: Bot/automated scripts with linear movements, constant speed, mechanical precision
- Detection goal: Identify automated bot activity from legitimate human users
- Features to analyze:
  1. Movement speed (pixels per millisecond)
  2. Path straightness (deviation from straight line)
  3. Pause frequency and duration
  4. Acceleration/deceleration patterns
  5. Click precision (distance from target center)

ML ALGORITHMS:
1. Isolation Forest - for unsupervised anomaly detection
2. Random Forest Classifier - for supervised classification
3. K-Means Clustering - for behavior grouping

DATASET SPECIFICATIONS:
- Generate 200 human user sessions (normal)
- Generate 50 bot sessions (anomalous)
- Each session: 20-50 mouse movements
- Include timestamps, x/y coordinates, click events
- Create 3 user types: "user_A" (human), "user_B" (human), "bot_detector_test" (mixed)

Please create all 3 Python files following the exact structure and style shown in the master template.
```

---

## 💡 Các Prompt Bổ Sung Hữu Ích

### 1. Khi Muốn Cải Thiện Code:
```
The code you provided is good, but please enhance it with:
1. More detailed comments explaining the security implications
2. Add a "Student Exercise" section where students modify parameters
3. Include a comparison table showing algorithm performance
4. Add more visualization showing feature distributions
5. Include a section explaining common evasion techniques
```

### 2. Khi Muốn Thêm Độ Khó:
```
Please create an advanced version of this lab that includes:
1. Adversarial examples - how attackers can evade detection
2. Feature engineering techniques
3. Hyperparameter tuning with GridSearchCV
4. Cross-validation for robust evaluation
5. ROC curves and AUC analysis
```

### 3. Khi Muốn Version Đơn Giản Hơn:
```
Please simplify this lab for absolute beginners by:
1. Reducing to only ONE ML algorithm (the simplest one)
2. Using smaller dataset (50-100 samples)
3. Adding step-by-step execution instructions
4. Including expected output examples in comments
5. Adding more explanatory print statements
```

---

## 📋 Checklist Để Kiểm Tra Output Của LLM

Sau khi LLM tạo code, kiểm tra:

- [ ] ✅ Code chạy được ngay (no errors)
- [ ] ✅ Dataset có patterns rõ ràng (visualize để xác nhận)
- [ ] ✅ Comments giải thích đầy đủ WHY, không chỉ WHAT
- [ ] ✅ Có verification script với plots
- [ ] ✅ ML algorithms được implement đúng
- [ ] ✅ Performance metrics được tính toán
- [ ] ✅ Visualizations rõ ràng và có label
- [ ] ✅ Print statements hữu ích cho học viên
- [ ] ✅ Có phần "Security Implications"
- [ ] ✅ Code structure professional và consistent

---

## 🎓 Tips Để Tạo Lab Hay

1. **Start với scenario thực tế**: Dựa trên tin tức bảo mật, CVE, hoặc incident reports
2. **Make patterns obvious**: Đừng tạo data quá khó - mục đích là học, không phải nghiên cứu
3. **Include failure cases**: Cho học viên thấy khi nào ML KHÔNG hoạt động tốt
4. **Add exercises**: Để học viên tự tay modify và experiment
5. **Document assumptions**: Giải thích rõ limitations của approach

Bạn có muốn tôi tạo thêm ví dụ cho một security scenario cụ thể nào không?
