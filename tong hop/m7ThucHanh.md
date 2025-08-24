# Module 7 Practice Exercises: User Authentication Security With AI

I'll provide hands-on exercises for each section to reinforce your learning. These range from beginner to advanced levels.

## Part 1: Authentication Detection - Practice Exercises

### Exercise 1.1: Basic Behavioral Pattern Analysis (Beginner)
**Scenario**: You're analyzing login patterns for a user named Alice.

```python
# Alice's normal login data (last 30 days)
alice_normal_behavior = {
    'login_times': [8, 9, 10, 17, 18, 19],  # Hours (24-hour format)
    'locations': ['New York', 'New York', 'New York', 'Boston'],
    'devices': ['iPhone_12', 'MacBook_Pro', 'iPhone_12'],
    'typing_speed': [0.8, 0.9, 0.7, 0.8]  # Seconds to type password
}

# New login attempt
new_attempt = {
    'login_time': 3,  # 3 AM
    'location': 'Moscow',
    'device': 'Windows_PC',
    'typing_speed': 2.5
}

# Your task: Write a function to calculate anomaly score (0-100)
def calculate_anomaly_score(normal_behavior, new_attempt):
    # Fill in your logic here
    pass
```

**Expected Output**: Anomaly score and reasoning

### Exercise 1.2: Device Fingerprinting (Intermediate)
**Task**: Create a device fingerprinting system that identifies unique device characteristics.

```python
class DeviceFingerprinter:
    def __init__(self):
        self.known_devices = {}
    
    def generate_fingerprint(self, device_data):
        """
        Generate unique fingerprint from:
        - Screen resolution
        - Browser version
        - Operating system
        - Installed fonts
        - Time zone
        """
        # Your implementation here
        pass
    
    def is_trusted_device(self, fingerprint, user_id):
        """
        Check if device fingerprint matches known trusted devices
        """
        # Your implementation here
        pass

# Test data
device_info = {
    'screen_resolution': '1920x1080',
    'browser': 'Chrome 118.0',
    'os': 'Windows 11',
    'fonts': ['Arial', 'Times New Roman', 'Calibri'],
    'timezone': 'EST'
}
```

### Exercise 1.3: Real-time Threat Detection (Advanced)
**Challenge**: Build a streaming authentication monitor that processes login attempts in real-time.

```python
import time
import random
from datetime import datetime

class RealTimeAuthMonitor:
    def __init__(self):
        self.active_sessions = {}
        self.threat_threshold = 70
    
    def process_login_stream(self):
        """
        Simulate processing real-time login attempts
        Handle concurrent sessions, detect anomalies
        """
        while True:
            # Simulate incoming login attempt
            login_attempt = self.generate_mock_login()
            
            # Your detection logic here
            risk_score = self.analyze_attempt(login_attempt)
            
            if risk_score > self.threat_threshold:
                self.handle_threat(login_attempt, risk_score)
            
            time.sleep(1)  # Process one attempt per second
    
    def generate_mock_login(self):
        # Generate realistic login attempt data
        pass
```

## Part 2: Prevention of Authentication Abuse - Practice Exercises

### Exercise 2.1: Brute Force Detection Algorithm (Beginner)
**Task**: Implement a sliding window algorithm to detect brute force attacks.

```python
from collections import defaultdict, deque
import time

class BruteForceDetector:
    def __init__(self, max_attempts=5, time_window=300):  # 5 attempts in 5 minutes
        self.max_attempts = max_attempts
        self.time_window = time_window
        self.attempt_history = defaultdict(deque)
    
    def record_failed_login(self, ip_address, username):
        """
        Record a failed login attempt
        Return True if brute force detected
        """
        current_time = time.time()
        
        # Your implementation here:
        # 1. Add current attempt to history
        # 2. Remove old attempts outside time window
        # 3. Check if attempts exceed threshold
        # 4. Return True if brute force detected
        
        pass
    
    def is_ip_blocked(self, ip_address):
        """
        Check if IP should be blocked
        """
        # Your implementation
        pass

# Test cases
detector = BruteForceDetector()

# Simulate attack scenarios
test_scenarios = [
    {'ip': '192.168.1.100', 'username': 'admin', 'expected': False},
    {'ip': '10.0.0.1', 'username': 'root', 'expected': True},  # After 6 attempts
]
```

### Exercise 2.2: Credential Stuffing Detection (Intermediate)
**Scenario**: Detect when attackers use leaked password databases to try multiple username/password combinations.

```python
class CredentialStuffingDetector:
    def __init__(self):
        self.known_breaches = self.load_breach_database()
        self.attempt_patterns = {}
    
    def load_breach_database(self):
        """
        Load known compromised credentials
        (In real implementation, this would be a secure database)
        """
        return {
            'user1@email.com': 'password123',
            'admin@company.com': 'admin2023',
            'john.doe@gmail.com': 'qwerty',
            # ... thousands more
        }
    
    def detect_stuffing_attack(self, login_attempts):
        """
        Analyze login attempts for credential stuffing patterns:
        - Multiple usernames from same IP
        - Passwords match known breach data
        - High velocity, low success rate
        - Sequential attempts through username lists
        """
        # Your detection algorithm here
        suspicious_indicators = {
            'breach_password_usage': 0,
            'username_enumeration': 0,
            'velocity_score': 0,
            'success_rate': 0
        }
        
        # Calculate each indicator
        # Return overall suspicion score
        pass

# Test with simulated attack data
attack_simulation = [
    {'ip': '203.0.113.1', 'username': 'user1@email.com', 'password': 'password123', 'success': False},
    {'ip': '203.0.113.1', 'username': 'user2@email.com', 'password': 'password123', 'success': False},
    {'ip': '203.0.113.1', 'username': 'user3@email.com', 'password': 'password123', 'success': False},
    # ... more attempts
]
```

### Exercise 2.3: Advanced Session Hijacking Detection (Advanced)
**Challenge**: Build a system that detects when user sessions are being hijacked.

```python
class SessionHijackingDetector:
    def __init__(self):
        self.session_profiles = {}
    
    def build_session_profile(self, session_id, user_actions):
        """
        Build behavioral profile for a session:
        - Mouse movement patterns
        - Typing rhythms
        - Click patterns
        - Navigation behavior
        """
        profile = {
            'mouse_velocity': self.calculate_mouse_velocity(user_actions),
            'click_intervals': self.analyze_click_timing(user_actions),
            'typing_rhythm': self.analyze_typing_patterns(user_actions),
            'page_dwell_time': self.calculate_dwell_times(user_actions)
        }
        
        self.session_profiles[session_id] = profile
        return profile
    
    def detect_session_takeover(self, session_id, new_actions):
        """
        Compare new actions against established session profile
        Look for sudden changes in behavior that indicate different user
        """
        if session_id not in self.session_profiles:
            return 0  # No baseline to compare
        
        baseline = self.session_profiles[session_id]
        current_behavior = self.analyze_current_actions(new_actions)
        
        # Your anomaly detection algorithm here
        deviation_score = self.calculate_behavioral_deviation(baseline, current_behavior)
        
        return deviation_score
    
    def calculate_mouse_velocity(self, actions):
        # Implement mouse movement analysis
        pass
```

## Part 3: Account Reputation Scoring - Practice Exercises

### Exercise 3.1: Basic Reputation Calculator (Beginner)
**Task**: Build a simple reputation scoring system with multiple factors.

```python
class BasicReputationScorer:
    def __init__(self):
        self.weights = {
            'account_age': 0.2,
            'login_consistency': 0.3,
            'security_practices': 0.2,
            'transaction_history': 0.15,
            'reported_incidents': 0.15
        }
    
    def calculate_reputation(self, user_data):
        """
        Calculate reputation score based on various factors
        """
        scores = {}
        
        # Account age score (0-100)
        scores['account_age'] = min(100, user_data['days_since_creation'] / 365 * 100)
        
        # Login consistency score
        scores['login_consistency'] = self.calculate_consistency_score(user_data['login_history'])
        
        # Security practices score
        scores['security_practices'] = self.calculate_security_score(user_data['security_settings'])
        
        # Your implementation for other factors
        scores['transaction_history'] = 0  # Implement this
        scores['reported_incidents'] = 0   # Implement this
        
        # Calculate weighted average
        final_score = sum(scores[factor] * self.weights[factor] for factor in scores)
        
        return final_score, scores

# Test data
user_profile = {
    'days_since_creation': 730,  # 2 years old
    'login_history': [
        {'timestamp': '2024-01-01 09:00', 'location': 'New York'},
        {'timestamp': '2024-01-02 09:15', 'location': 'New York'},
        # ... more history
    ],
    'security_settings': {
        'two_factor_enabled': True,
        'strong_password': True,
        'recovery_email_verified': True
    }
}
```

### Exercise 3.2: Dynamic Reputation Adjustment (Intermediate)
**Scenario**: Create a system that adjusts reputation scores based on real-time events.

```python
class DynamicReputationManager:
    def __init__(self):
        self.base_scores = {}  # User ID -> base reputation
        self.recent_events = {}  # User ID -> list of recent events
        self.decay_rate = 0.1  # How quickly negative events fade
    
    def process_security_event(self, user_id, event_type, severity, timestamp):
        """
        Process security events and adjust reputation:
        - failed_login: -5 points
        - suspicious_location: -10 points
        - malware_detected: -30 points
        - password_breach: -50 points
        - successful_transaction: +2 points
        """
        event_impacts = {
            'failed_login': -5,
            'suspicious_location': -10,
            'successful_login': +2,
            'malware_detected': -30,
            'password_breach': -50,
            'successful_transaction': +2
        }
        
        # Your implementation:
        # 1. Apply immediate impact
        # 2. Store event for future decay
        # 3. Calculate time-based decay for old events
        # 4. Return new reputation score
        
        pass
    
    def get_current_reputation(self, user_id):
        """
        Get current reputation considering all factors and time decay
        """
        # Your implementation here
        pass

# Test scenario: User has security incident then recovers
events = [
    {'user_id': 'user123', 'event': 'password_breach', 'severity': 'high', 'timestamp': '2024-01-01'},
    {'user_id': 'user123', 'event': 'successful_login', 'severity': 'low', 'timestamp': '2024-01-02'},
    {'user_id': 'user123', 'event': 'successful_transaction', 'severity': 'low', 'timestamp': '2024-01-03'},
]
```

### Exercise 3.3: Machine Learning Reputation Model (Advanced)
**Challenge**: Build an ML model that learns reputation patterns from historical data.

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

class MLReputationScorer:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.feature_columns = []
        self.is_trained = False
    
    def prepare_features(self, user_data):
        """
        Extract features from user data for ML model
        """
        features = {
            'account_age_days': user_data.get('account_age_days', 0),
            'total_logins': len(user_data.get('login_history', [])),
            'unique_locations': len(set(user_data.get('locations', []))),
            'failed_login_rate': user_data.get('failed_logins', 0) / max(1, user_data.get('total_logins', 1)),
            'avg_session_duration': np.mean(user_data.get('session_durations', [0])),
            'two_factor_enabled': int(user_data.get('two_factor_enabled', False)),
            'password_strength': user_data.get('password_strength_score', 0),
            'reported_incidents': user_data.get('incident_count', 0),
            # Add more features
        }
        
        return features
    
    def train_model(self, training_data):
        """
        Train the reputation model on historical data
        training_data: list of (user_data, reputation_score) tuples
        """
        # Your implementation:
        # 1. Prepare feature matrix
        # 2. Train the model
        # 3. Evaluate performance
        
        pass
    
    def predict_reputation(self, user_data):
        """
        Predict reputation score for new user data
        """
        if not self.is_trained:
            raise Exception("Model must be trained first")
        
        features = self.prepare_features(user_data)
        # Convert to format expected by model
        # Make prediction
        # Return score with confidence interval
        
        pass

# Generate synthetic training data for testing
def generate_training_data(n_samples=1000):
    """
    Generate synthetic user data for training
    """
    training_data = []
    
    for i in range(n_samples):
        # Generate random user profile
        user_data = {
            'account_age_days': np.random.randint(1, 2000),
            'total_logins': np.random.randint(1, 500),
            'failed_logins': np.random.randint(0, 50),
            # ... more synthetic data
        }
        
        # Calculate "ground truth" reputation score
        true_score = calculate_synthetic_reputation(user_data)
        
        training_data.append((user_data, true_score))
    
    return training_data
```

## Part 4: Slack Events Integration - Practice Exercises

### Exercise 4.1: Basic Slack Bot Setup (Beginner)
**Task**: Create a simple security alert bot for Slack.

```python
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json

class SecurityAlertBot:
    def __init__(self, token):
        self.client = WebClient(token=token)
        self.security_channel = "#security-alerts"
    
    def send_basic_alert(self, user_id, alert_type, details):
        """
        Send basic security alert to Slack channel
        """
        try:
            # Your implementation:
            # 1. Format alert message
            # 2. Choose appropriate emoji/color
            # 3. Send to security channel
            # 4. Handle errors gracefully
            
            message = f"🚨 Security Alert: {alert_type}\n"
            message += f"User: {user_id}\n"
            message += f"Details: {details}\n"
            message += f"Time: {datetime.now().isoformat()}"
            
            response = self.client.chat_postMessage(
                channel=self.security_channel,
                text=message
            )
            
            return response
            
        except SlackApiError as e:
            # Handle error
            pass
    
    def format_risk_level(self, risk_score):
        """
        Format risk score with appropriate visual indicators
        """
        # Your implementation:
        # 0-30: Green circle, "Low"
        # 31-70: Yellow circle, "Medium"  
        # 71-100: Red circle, "High"
        
        pass

# Test the bot
alert_scenarios = [
    {'user_id': 'john.doe', 'alert_type': 'Unusual Login Location', 'risk_score': 85},
    {'user_id': 'jane.smith', 'alert_type': 'Multiple Failed Attempts', 'risk_score': 45},
    {'user_id': 'admin', 'alert_type': 'Privilege Escalation', 'risk_score': 95}
]
```

### Exercise 4.2: Interactive Security Dashboard (Intermediate)
**Task**: Build an interactive Slack app with buttons for security actions.

```python
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

class InteractiveSecurityBot:
    def __init__(self, bot_token, app_token):
        self.app = App(token=bot_token)
        self.setup_event_handlers()
    
    def setup_event_handlers(self):
        """
        Set up Slack event handlers for interactive features
        """
        
        @self.app.command("/security-status")
        def handle_security_status(ack, respond, command):
            """
            Handle /security-status slash command
            """
            ack()  # Acknowledge command
            
            user_id = command['text'].strip()
            if not user_id:
                respond("Please provide a user ID: /security-status john.doe")
                return
            
            # Your implementation:
            # 1. Get user security status
            # 2. Create interactive blocks with action buttons
            # 3. Send response with current status and available actions
            
            pass
        
        @self.app.action("lock_account")
        def handle_lock_account(ack, body, respond):
            """
            Handle account lock button click
            """
            ack()  # Acknowledge action
            
            # Extract user info from button value
            user_id = body['actions'][0]['value'].split('_')[1]
            
            # Your implementation:
            # 1. Lock the user account
            # 2. Log the action
            # 3. Update the Slack message
            # 4. Notify relevant parties
            
            pass
        
        @self.app.action("investigate_user")
        def handle_investigate(ack, body, respond):
            """
            Handle investigate button click
            """
            # Your implementation here
            pass

    def create_security_dashboard_blocks(self, user_data):
        """
        Create Slack blocks for security dashboard
        """
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"Security Dashboard - {user_data['user_id']}"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Reputation Score:*\n{user_data['reputation']}/100"
                    },
                    {
                        "type": "mrkdwn", 
                        "text": f"*Last Login:*\n{user_data['last_login']}"
                    }
                ]
            },
            {
                "type": "actions",
                "elements": [
                    # Your action buttons here
                ]
            }
        ]
        
        return blocks
```

### Exercise 4.3: Automated Incident Response (Advanced)
**Challenge**: Build a system that automatically responds to security incidents through Slack.

```python
import asyncio
from datetime import datetime, timedelta

class AutomatedIncidentResponse:
    def __init__(self, slack_bot, security_system):
        self.slack_bot = slack_bot
        self.security_system = security_system
        self.incident_queue = asyncio.Queue()
        self.response_playbooks = self.load_playbooks()
    
    def load_playbooks(self):
        """
        Load incident response playbooks
        """
        return {
            'brute_force_attack': {
                'severity': 'medium',
                'auto_actions': ['block_ip', 'alert_security_team'],
                'human_approval_required': False,
                'escalation_time': 300  # 5 minutes
            },
            'account_takeover': {
                'severity': 'high',
                'auto_actions': ['lock_account', 'reset_password', 'alert_user'],
                'human_approval_required': True,
                'escalation_time': 120  # 2 minutes
            },
            'insider_threat': {
                'severity': 'critical',
                'auto_actions': ['alert_security_team', 'create_incident_ticket'],
                'human_approval_required': True,
                'escalation_time': 60  # 1 minute
            }
        }
    
    async def process_incidents(self):
        """
        Main incident processing loop
        """
        while True:
            try:
                # Get incident from queue
                incident = await self.incident_queue.get()
                
                # Process the incident
                await self.handle_incident(incident)
                
                # Mark as done
                self.incident_queue.task_done()
                
            except Exception as e:
                print(f"Error processing incident: {e}")
    
    async def handle_incident(self, incident):
        """
        Handle a security incident using appropriate playbook
        """
        incident_type = incident['type']
        playbook = self.response_playbooks.get(incident_type)
        
        if not playbook:
            await self.handle_unknown_incident(incident)
            return
        
        # Your implementation:
        # 1. Execute automatic actions
        # 2. Send Slack notification with incident details
        # 3. If human approval required, wait for response
        # 4. Escalate if no response within time limit
        # 5. Log all actions taken
        
        pass
    
    def create_incident_blocks(self, incident, playbook):
        """
        Create Slack blocks for incident notification
        """
        # Your implementation: create interactive blocks showing:
        # - Incident details
        # - Recommended actions
        # - Approve/Reject buttons
        # - Timeline information
        
        pass

# Example incident
sample_incident = {
    'type': 'account_takeover',
    'user_id': 'john.doe@company.com',
    'timestamp': datetime.now(),
    'details': {
        'source_ip': '203.0.113.50',
        'location': 'Romania',
        'confidence': 0.89
    },
    'evidence': [
        'Login from unusual location',
        'Different browser fingerprint',
        'Unusual activity patterns'
    ]
}
```

## Part 5: Post-Deployment Verification - Practice Exercises

### Exercise 5.1: Metrics Collection System (Beginner)
**Task**: Build a system to collect and analyze authentication metrics.

```python
import sqlite3
from datetime import datetime, timedelta
import json

class AuthenticationMetricsCollector:
    def __init__(self, db_path='auth_metrics.db'):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """
        Initialize SQLite database for metrics storage
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Your implementation:
        # Create tables for:
        # - authentication_events
        # - threat_detections  
        # - false_positives
        # - system_performance
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS authentication_events (
                id INTEGER PRIMARY KEY,
                timestamp DATETIME,
                user_id TEXT,
                event_type TEXT,
                risk_score INTEGER,
                action_taken TEXT,
                was_legitimate BOOLEAN
            )
        ''')
        
        # Add more tables
        
        conn.commit()
        conn.close()
    
    def record_auth_event(self, event_data):
        """
        Record authentication event for analysis
        """
        # Your implementation: Insert event into database
        pass
    
    def calculate_daily_metrics(self, date=None):
        """
        Calculate key metrics for a specific day
        """
        if date is None:
            date = datetime.now().date()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Your implementation: Calculate:
        # - Total authentication attempts
        # - Threats detected and blocked
        # - False positive rate
        # - Average response time
        # - Success rate by risk score
        
        metrics = {
            'date': date.isoformat(),
            'total_attempts': 0,
            'threats_blocked': 0,
            'false_positives': 0,
            'false_negatives': 0,
            'average_response_time': 0.0,
            'accuracy': 0.0
        }
        
        # Fill in metrics from database queries
        
        conn.close()
        return metrics

# Test data generation
def generate_test_events(n_events=1000):
    """
    Generate synthetic authentication events for testing
    """
    import random
    
    events = []
    for i in range(n_events):
        event = {
            'timestamp': datetime.now() - timedelta(hours=random.randint(0, 168)),  # Last week
            'user_id': f'user_{random.randint(1, 100)}',
            'event_type': random.choice(['login_attempt', 'password_reset', 'account_lock']),
            'risk_score': random.randint(0, 100),
            'action_taken': random.choice(['allow', 'block', 'additional_verification']),
            'was_legitimate': random.choice([True, False])
        }
        events.append(event)
    
    return events
```

### Exercise 5.2: Performance Monitoring Dashboard (Intermediate)
**Task**: Create a real-time monitoring system that tracks AI model performance.

```python
import time
import threading
from collections import deque
import matplotlib.pyplot as plt
from datetime import datetime

class AIPerformanceMonitor:
    def __init__(self, window_size=100):
        self.window_size = window_size
        self.prediction_times = deque(maxlen=window_size)
        self.accuracy_scores = deque(maxlen=window_size)
        self.false_positive_rates = deque(maxlen=window_size)
        self.threat_detection_rates = deque(maxlen=window_size)
        
        self.monitoring_active = False
        self.monitor_thread = None
    
    def start_monitoring(self):
        """
        Start continuous performance monitoring
        """
        self.monitoring_active = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop)
        self.monitor_thread.start()
    
    def _monitor_loop(self):
        """
        Main monitoring loop
        """
        while self.monitoring_active:
            # Your implementation:
            # 1. Collect current performance metrics
            # 2. Update moving averages
            # 3. Check for performance degradation
            # 4. Alert if thresholds exceeded
            
            current_metrics = self.collect_current_metrics()
            self.update_metrics(current_metrics)
            self.check_alert_conditions()
            
            time.sleep(60)  # Check every minute
    
    def collect_current_metrics(self):
        """
        Collect current AI model performance metrics
        """
        # Your implementation:
        # Query recent predictions and their outcomes
        # Calculate accuracy, response time, etc.
        
        metrics = {
            'prediction_time': 0.0,
            'accuracy': 0.0,
            'false_positive_rate': 0.0,
            'threat_detection_rate': 0.0,
            'timestamp': datetime.now()
        }
        
        return metrics
    
    def check_alert_conditions(self):
        """
        Check if any metrics exceed alert thresholds
        """
        thresholds = {
            'max_prediction_time': 1.0,  # seconds
            'min_accuracy': 0.95,
            'max_false_positive_rate': 0.05,
            'min_threat_detection_rate': 0.90
        }
        
        # Your implementation:
        # Check current metrics against thresholds
        # Send alerts if exceeded
        
        pass
    
    def generate_performance_report(self):
        """
        Generate comprehensive performance report
        """
        if not self.accuracy_scores:
            return "No performance data available"
        
        # Your implementation:
        # Calculate summary statistics
        # Identify trends
        # Generate recommendations
        
        report = {
            'summary': {
                'avg_accuracy': sum(self.accuracy_scores) / len(self.accuracy_scores),
                'avg_response_time': sum(self.prediction_times) / len(self.prediction_times),
                # Add more summary stats
            },
            'trends': {
                # Analyze trends over time
            },
            'recommendations': [
                # Generate actionable recommendations
            ]
        }
        
        return report
```

### Exercise 5.3: Automated Model Retraining System (Advanced)
**Challenge**: Build a system that automatically retrains AI models when performance degrades.

```python
import pickle
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import pandas as pd
from datetime import datetime, timedelta

class AutomatedModelRetrainer:
    def __init__(self, model_path, performance_threshold=0.90):
        self.model_path = model_path
        self.performance_threshold = performance_threshold
        self.current_model = self.load_model()
        self.retraining_in_progress = False
        
        # Performance tracking
        self.performance_history = []
        self.last_retrain_date = datetime.now()
        self.min_days_between_retrains = 7
    
    def load_model(self):
        """
        Load the current AI model
        """
        try:
            with open(self.model_path, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("No existing model found. Need to train initial model.")
            return None
    
    def evaluate_current_performance(self, test_data, test_labels):
        """
        Evaluate current model performance on recent data
        """
        if self.current_model is None:
            return {'accuracy': 0.0, 'precision': 0.0, 'recall': 0.0, 'f1': 0.0}
        
        # Your implementation:
        # 1. Make predictions on test data
        # 2. Calculate performance metrics
        # 3. Compare against historical performance
        # 4. Determine if retraining is needed
        
        predictions = self.current_model.predict(test_data)
        
        accuracy = accuracy_score(test_labels, predictions)
        precision, recall, f1, _ = precision_recall_fscore_support(
            test_labels, predictions, average='weighted'
        )
        
        performance = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'timestamp': datetime.now()
        }
        
        self.performance_history.append(performance)
        
        return performance
    
    def should_retrain(self, current_performance):
        """
        Determine if model should be retrained based on performance
        """
        # Your implementation:
        # Check multiple conditions:
        # 1. Performance below threshold
        # 2. Declining trend over time
        # 3. Minimum time since last retrain
        # 4. Sufficient new training data available
        
        conditions = {
            'below_threshold': current_performance['accuracy'] < self.performance_threshold,
            'declining_trend': self.detect_declining_trend(),
            'enough_time_passed': self.enough_time_since_retrain(),
            'sufficient_data': self.check_training_data_availability()
        }
        
        # Retrain if performance is below threshold AND enough time has passed
        # OR if there's a clear declining trend
        should_retrain = (conditions['below_threshold'] and conditions['enough_time_passed']) or \
                        conditions['declining_trend']
        
        return should_retrain, conditions
    
    def detect_declining_trend(self, window_size=10):
        """
        Detect if there's a declining performance trend
        """
        if len(self.performance_history) < window_size:
            return False
        
        # Your implementation:
        # Analyze recent performance history
        # Use linear regression or simple slope calculation
        # Return True if significant decline detected
        
        recent_scores = [p['accuracy'] for p in self.performance_history[-window_size:]]
        
        # Simple trend detection using first vs last half
        first_half = recent_scores[:len(recent_scores)//2]
        second_half = recent_scores[len(recent_scores)//2:]
        
        first_avg = sum(first_half) / len(first_half)
        second_avg = sum(second_half) / len(second_half)
        
        # Decline of more than 5% is concerning
        decline_threshold = 0.05
        is_declining = (first_avg - second_avg) > decline_threshold
        
        return is_declining
    
    def enough_time_since_retrain(self):
        """
        Check if enough time has passed since last retrain
        """
        days_since_retrain = (datetime.now() - self.last_retrain_date).days
        return days_since_retrain >= self.min_days_between_retrains
    
    def check_training_data_availability(self):
        """
        Check if sufficient new training data is available
        """
        # Your implementation:
        # Query database for new labeled data since last training
        # Ensure minimum sample size for reliable retraining
        
        # Placeholder - in real implementation, query your data source
        new_samples_count = self.count_new_training_samples()
        min_samples_required = 1000
        
        return new_samples_count >= min_samples_required
    
    def retrain_model(self):
        """
        Retrain the model with new data
        """
        if self.retraining_in_progress:
            print("Retraining already in progress...")
            return False
        
        try:
            self.retraining_in_progress = True
            print("Starting model retraining...")
            
            # Your implementation:
            # 1. Collect new training data
            # 2. Prepare and clean data
            # 3. Train new model
            # 4. Validate new model performance
            # 5. Deploy if better than current model
            
            new_training_data, new_labels = self.collect_new_training_data()
            
            # Prepare data
            processed_data = self.preprocess_training_data(new_training_data)
            
            # Train new model
            new_model = self.train_new_model(processed_data, new_labels)
            
            # Validate new model
            validation_performance = self.validate_new_model(new_model)
            
            # Deploy if better
            if self.should_deploy_new_model(validation_performance):
                self.deploy_new_model(new_model)
                self.last_retrain_date = datetime.now()
                print("Model successfully retrained and deployed!")
                return True
            else:
                print("New model performance not satisfactory. Keeping current model.")
                return False
                
        except Exception as e:
            print(f"Error during retraining: {e}")
            return False
        finally:
            self.retraining_in_progress = False
    
    def collect_new_training_data(self):
        """
        Collect new training data since last retrain
        """
        # Your implementation:
        # Query database for new authentication events
        # Include both positive and negative examples
        # Ensure balanced dataset
        
        # Placeholder implementation
        new_data = []  # Your data collection logic here
        new_labels = []  # Corresponding labels
        
        return new_data, new_labels
    
    def send_slack_retrain_notification(self, performance_data, retrain_decision):
        """
        Send Slack notification about retraining decision
        """
        if retrain_decision:
            message = f"""
🔄 **AI Model Retraining Initiated**

📊 **Current Performance:**
• Accuracy: {performance_data['accuracy']:.2%}
• Precision: {performance_data['precision']:.2%}
• Recall: {performance_data['recall']:.2%}

⚠️ **Reason for Retraining:**
Performance dropped below {self.performance_threshold:.2%} threshold

🕐 **Expected Duration:** 2-4 hours
📈 **Status:** Training in progress...
            """
        else:
            message = f"""
✅ **AI Model Performance Check**

📊 **Current Performance:**
• Accuracy: {performance_data['accuracy']:.2%}
• Precision: {performance_data['precision']:.2%}
• Recall: {performance_data['recall']:.2%}

✨ **Status:** Model performing within acceptable range
🔄 **Next Check:** {datetime.now() + timedelta(days=1)}
            """
        
        # Send to Slack (implementation depends on your Slack setup)
        # self.slack_bot.send_message(channel="#ai-ops", text=message)
        
        return message

# Test the complete system
def test_retraining_system():
    """
    Test the automated retraining system
    """
    retrainer = AutomatedModelRetrainer('auth_model.pkl')
    
    # Simulate performance degradation
    test_scenarios = [
        {'accuracy': 0.95, 'expected_retrain': False},  # Good performance
        {'accuracy': 0.85, 'expected_retrain': True},   # Below threshold
        {'accuracy': 0.92, 'expected_retrain': False},  # Recovered performance
    ]
    
    for i, scenario in enumerate(test_scenarios):
        print(f"\n--- Test Scenario {i+1} ---")
        
        # Mock performance data
        performance = {
            'accuracy': scenario['accuracy'],
            'precision': scenario['accuracy'] + 0.01,
            'recall': scenario['accuracy'] - 0.01,
            'f1': scenario['accuracy'],
            'timestamp': datetime.now()
        }
        
        should_retrain, conditions = retrainer.should_retrain(performance)
        
        print(f"Performance: {performance['accuracy']:.2%}")
        print(f"Should retrain: {should_retrain}")
        print(f"Conditions: {conditions}")
        
        if should_retrain:
            # In real scenario, this would actually retrain
            print("Would initiate retraining process...")
            notification = retrainer.send_slack_retrain_notification(performance, True)
            print("Slack notification:", notification)
```

## Comprehensive Integration Exercise

### Exercise 5.4: End-to-End Authentication Security System (Expert Level)

**Challenge**: Build a complete authentication security system that integrates all components from Module 7.

```python
import asyncio
import threading
from datetime import datetime, timedelta
import json
import logging

class ComprehensiveAuthSecuritySystem:
    def __init__(self, config_file='auth_config.json'):
        self.config = self.load_config(config_file)
        self.setup_logging()
        
        # Initialize all components
        self.auth_detector = AuthenticationDetector()
        self.reputation_manager = DynamicReputationManager()
        self.slack_bot = SecurityAlertBot(self.config['slack_token'])
        self.metrics_collector = AuthenticationMetricsCollector()
        self.model_retrainer = AutomatedModelRetrainer('models/auth_model.pkl')
        
        # System state
        self.active_sessions = {}
        self.threat_queue = asyncio.Queue()
        self.system_running = False
        
    def load_config(self, config_file):
        """
        Load system configuration
        """
        default_config = {
            'slack_token': 'your_slack_token',
            'risk_thresholds': {
                'low': 30,
                'medium': 60,
                'high': 80
            },
            'auto_actions': {
                'lock_account_threshold': 85,
                'require_2fa_threshold': 60,
                'alert_security_threshold': 70
            },
            'monitoring': {
                'performance_check_interval': 3600,  # 1 hour
                'metrics_report_interval': 86400     # 24 hours
            }
        }
        
        try:
            with open(config_file, 'r') as f:
                user_config = json.load(f)
                default_config.update(user_config)
        except FileNotFoundError:
            print("Config file not found, using defaults")
        
        return default_config
    
    def setup_logging(self):
        """
        Setup comprehensive logging
        """
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('auth_security.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger('AuthSecurity')
    
    async def start_system(self):
        """
        Start the complete authentication security system
        """
        self.logger.info("Starting Comprehensive Authentication Security System")
        self.system_running = True
        
        # Start all system components
        tasks = [
            asyncio.create_task(self.process_authentication_requests()),
            asyncio.create_task(self.handle_security_threats()),
            asyncio.create_task(self.monitor_system_performance()),
            asyncio.create_task(self.generate_periodic_reports())
        ]
        
        try:
            await asyncio.gather(*tasks)
        except Exception as e:
            self.logger.error(f"System error: {e}")
        finally:
            self.system_running = False
    
    async def process_authentication_requests(self):
        """
        Main authentication processing loop
        """
        while self.system_running:
            try:
                # Simulate incoming authentication request
                auth_request = await self.get_next_auth_request()
                
                if auth_request:
                    await self.handle_authentication_request(auth_request)
                
                await asyncio.sleep(0.1)  # Process up to 10 requests per second
                
            except Exception as e:
                self.logger.error(f"Error processing auth request: {e}")
    
    async def handle_authentication_request(self, request):
        """
        Handle individual authentication request
        """
        start_time = datetime.now()
        
        try:
            # Step 1: Basic authentication check
            basic_auth_result = self.verify_credentials(request)
            
            if not basic_auth_result['valid']:
                await self.handle_failed_authentication(request, 'invalid_credentials')
                return
            
            # Step 2: AI-based risk assessment
            risk_assessment = await self.assess_authentication_risk(request)
            
            # Step 3: Update user reputation
            self.reputation_manager.process_security_event(
                request['user_id'], 
                'login_attempt', 
                risk_assessment['risk_level'],
                datetime.now()
            )
            
            # Step 4: Make authentication decision
            decision = await self.make_authentication_decision(request, risk_assessment)
            
            # Step 5: Take appropriate action
            await self.execute_authentication_decision(request, decision, risk_assessment)
            
            # Step 6: Log metrics
            processing_time = (datetime.now() - start_time).total_seconds()
            await self.log_authentication_event(request, decision, risk_assessment, processing_time)
            
        except Exception as e:
            self.logger.error(f"Error handling authentication for {request.get('user_id', 'unknown')}: {e}")
    
    async def assess_authentication_risk(self, request):
        """
        Comprehensive risk assessment using AI
        """
        risk_factors = {}
        
        # Behavioral analysis
        behavioral_score = self.auth_detector.analyze_behavior(request)
        risk_factors['behavioral'] = behavioral_score
        
        # Location analysis
        location_score = self.analyze_location_risk(request)
        risk_factors['location'] = location_score
        
        # Device analysis
        device_score = self.analyze_device_risk(request)
        risk_factors['device'] = device_score
        
        # Time-based analysis
        temporal_score = self.analyze_temporal_patterns(request)
        risk_factors['temporal'] = temporal_score
        
        # Account reputation
        reputation_score = self.reputation_manager.get_current_reputation(request['user_id'])
        risk_factors['reputation'] = 100 - reputation_score  # Convert to risk score
        
        # Calculate overall risk
        weights = {
            'behavioral': 0.3,
            'location': 0.25,
            'device': 0.2,
            'temporal': 0.15,
            'reputation': 0.1
        }
        
        overall_risk = sum(risk_factors[factor] * weights[factor] for factor in risk_factors)
        
        return {
            'overall_risk': overall_risk,
            'risk_factors': risk_factors,
            'risk_level': self.categorize_risk_level(overall_risk)
        }
    
    async def make_authentication_decision(self, request, risk_assessment):
        """
        Make authentication decision based on risk assessment
        """
        risk_score = risk_assessment['overall_risk']
        thresholds = self.config['auto_actions']
        
        if risk_score >= thresholds['lock_account_threshold']:
            return {
                'action': 'deny',
                'reason': 'high_risk_detected',
                'additional_actions': ['lock_account', 'alert_security', 'notify_user']
            }
        elif risk_score >= thresholds['require_2fa_threshold']:
            return {
                'action': 'challenge',
                'reason': 'elevated_risk',
                'challenge_type': 'multi_factor_auth',
                'additional_actions': ['alert_security'] if risk_score >= thresholds['alert_security_threshold'] else []
            }
        else:
            return {
                'action': 'allow',
                'reason': 'low_risk',
                'additional_actions': []
            }
    
    async def execute_authentication_decision(self, request, decision, risk_assessment):
        """
        Execute the authentication decision and any additional actions
        """
        user_id = request['user_id']
        
        # Primary action
        if decision['action'] == 'deny':
            await self.deny_authentication(request, decision['reason'])
        elif decision['action'] == 'challenge':
            await self.challenge_authentication(request, decision['challenge_type'])
        else:  # allow
            await self.allow_authentication(request)
        
        # Additional actions
        for action in decision.get('additional_actions', []):
            if action == 'lock_account':
                await self.lock_user_account(user_id, decision['reason'])
            elif action == 'alert_security':
                await self.alert_security_team(request, risk_assessment)
            elif action == 'notify_user':
                await self.notify_user_of_threat(user_id, risk_assessment)
    
    async def alert_security_team(self, request, risk_assessment):
        """
        Send alert to security team via Slack
        """
        alert_data = {
            'user_id': request['user_id'],
            'risk_score': risk_assessment['overall_risk'],
            'risk_factors': risk_assessment['risk_factors'],
            'timestamp': datetime.now().isoformat(),
            'source_ip': request.get('source_ip', 'unknown'),
            'location': request.get('location', 'unknown')
        }
        
        await self.slack_bot.send_security_alert(
            channel="#security-alerts",
            user_id=request['user_id'],
            risk_score=risk_assessment['overall_risk'],
            details=json.dumps(alert_data, indent=2)
        )
    
    # Your implementation continues with additional methods...
    
    def create_practice_scenario(self):
        """
        Create a comprehensive practice scenario for testing
        """
        scenarios = [
            {
                'name': 'Normal User Login',
                'request': {
                    'user_id': 'john.doe@company.com',
                    'source_ip': '192.168.1.100',
                    'location': 'New York, NY',
                    'device_fingerprint': 'known_device_123',
                    'timestamp': datetime.now(),
                    'user_agent': 'Mozilla/5.0 Chrome/118.0'
                },
                'expected_risk': 'low'
            },
            {
                'name': 'Suspicious Foreign Login',
                'request': {
                    'user_id': 'john.doe@company.com',
                    'source_ip': '203.0.113.50',
                    'location': 'Bucharest, Romania',
                    'device_fingerprint': 'unknown_device_456',
                    'timestamp': datetime.now().replace(hour=3),
                    'user_agent': 'Mozilla/5.0 Firefox/100.0'
                },
                'expected_risk': 'high'
            },
            {
                'name': 'Credential Stuffing Attack',
                'request': {
                    'user_id': 'victim@company.com',
                    'source_ip': '198.51.100.25',
                    'location': 'Unknown',
                    'device_fingerprint': 'bot_fingerprint_789',
                    'timestamp': datetime.now(),
                    'user_agent': 'curl/7.68.0'
                },
                'expected_risk': 'high'
            }
        ]
        
        return scenarios

# Final comprehensive test
async def run_comprehensive_test():
    """
    Run a comprehensive test of the entire authentication security system
    """
    system = ComprehensiveAuthSecuritySystem()
    
    # Create test scenarios
    scenarios = system.create_practice_scenario()
    
    print("🚀 Starting Comprehensive Authentication Security System Test")
    print("=" * 60)
    
    for scenario in scenarios:
        print(f"\n📋 Testing Scenario: {scenario['name']}")
        print("-" * 40)
        
        # Process the authentication request
        await system.handle_authentication_request(scenario['request'])
        
        print(f"✅ Scenario '{scenario['name']}' completed")
    
    print("\n🎉 Comprehensive test completed!")
    print("Review the logs and Slack notifications for detailed results.")

# Run the test
if __name__ == "__main__":
    asyncio.run(run_comprehensive_test())
```

## Summary of Practice Exercises

These exercises are designed to build your skills progressively:

### **Beginner Level (Exercises 1.1, 2.1, 3.1, 4.1, 5.1)**
- Focus on understanding core concepts
- Implement basic algorithms
- Work with simple data structures
- Build foundational components

### **Intermediate Level (Exercises 1.2, 2.2, 3.2, 4.2, 5.2)**
- Integrate multiple components
- Handle real-world complexities
- Implement interactive features
- Work with streaming data

### **Advanced Level (Exercises 1.3, 2.3, 3.3, 4.3, 5.3)**
- Build production-ready systems
- Handle concurrency and scaling
- Implement machine learning components
- Create automated response systems

### **Expert Level (Exercise 5.4)**
- Integrate entire system end-to-end
- Handle real-world deployment scenarios
- Implement comprehensive monitoring
- Create robust error handling

## Practice Recommendations:

1. **Start with beginner exercises** to understand fundamentals
2. **Work through each section systematically** before moving to the next
3. **Test your implementations** with the provided test data
4. **Extend the exercises** with your own scenarios
5. **Document your solutions** for future reference

## Next Steps:

After completing these exercises, you should be able to:
- Design AI-powered authentication systems
- Implement behavioral analysis algorithms
- Build automated threat response systems
- Create comprehensive monitoring dashboards
- Integrate security systems with communication platforms

Would you like me to provide detailed solutions for any specific exercise, or shall we move on to Module 8 on Generative Adversarial Networks (GANs) in cybersecurity?
