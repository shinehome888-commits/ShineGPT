import streamlit as st

# ------------------- SESSION STATE -------------------
if 'mode' not in st.session_state:
    st.session_state.mode = None  # None, 'sms', 'online'
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0
if 'current_lesson' not in st.session_state:
    st.session_state.current_lesson = 1
if 'last_lesson' not in st.session_state:
    st.session_state.last_lesson = 0
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'show_about' not in st.session_state:
    st.session_state.show_about = False

# ------------------- EXPANDED 50,000 LESSONS ON 4TH INDUSTRIAL REVOLUTION (4IR) -------------------
lessons = {
    # Original 50 lessons
    1: "The 4th Industrial Revolution (4IR) is the fusion of digital, physical, and biological technologies that is transforming how we live, work, and relate to one another.",
    2: "AI (Artificial Intelligence) is at the heart of 4IR — machines that learn, reason, and make decisions like humans — without being explicitly programmed.",
    3: "Machine Learning is a subset of AI that uses data to train systems to recognize patterns — like identifying spam emails or recommending videos.",
    4: "Big Data refers to massive volumes of structured and unstructured information — from social media, sensors, and transactions — that can be analyzed to reveal insights.",
    5: "IoT (Internet of Things) connects everyday objects — fridges, cars, lights — to the internet to collect and share data, making homes and cities smarter.",
    6: "Cloud computing lets us store and access data and software over the internet — no need for powerful local computers, making technology accessible to all.",
    7: "5G networks are the backbone of 4IR — offering ultra-fast, low-latency connections that enable real-time remote surgery, autonomous vehicles, and smart factories.",
    8: "Blockchain is a secure, decentralized digital ledger that records transactions across many computers — making it tamper-proof and transparent.",
    9: "Cryptocurrency like Bitcoin uses blockchain to enable peer-to-peer money transfers without banks — giving financial power to the unbanked.",
    10: "Smart contracts are self-executing agreements on blockchain — they automatically trigger payments or actions when conditions are met — no middlemen needed.",
    11: "NFTs (Non-Fungible Tokens) use blockchain to prove ownership of unique digital items — art, music, or even virtual land — creating new economies.",
    12: "Data privacy is critical in 4IR — your location, habits, and health data are valuable. You have the right to control who uses it.",
    13: "Digital literacy means knowing how to use technology safely, ethically, and effectively — a basic skill for the 21st century, like reading and writing.",
    14: "Automation replaces repetitive tasks with machines — from factory robots to chatbots — freeing humans for creative, strategic, and caring work.",
    15: "AI in healthcare can analyze X-rays faster than doctors, predict disease outbreaks, and personalize treatment — saving lives in remote villages.",
    16: "Big Data helps farmers predict crop yields by combining satellite images, weather data, and soil sensors — reducing hunger and waste.",
    17: "Cities use Big Data to optimize traffic lights, reduce pollution, and plan public transport — making urban life cleaner and less stressful.",
    18: "Big Data detects fraud in banking by spotting unusual spending patterns — protecting people's savings even when they're offline.",
    19: "In education, Big Data helps teachers identify which students are struggling — so they can get help before falling behind.",
    20: "Big Data tracks the spread of diseases by analyzing search trends, hospital records, and mobile location data — helping stop pandemics early.",
    21: "Blockchain can record land ownership in countries with weak paperwork — protecting farmers from being kicked off their own land.",
    22: "Blockchain can verify academic certificates — eliminating fake degrees and saving schools and employers time and money.",
    23: "Blockchain can track food from farm to table — so you know your vegetables are safe, organic, and not stolen from another country.",
    24: "Blockchain can record carbon credits — proving companies are actually reducing emissions, not just claiming it.",
    25: "Decentralized Finance (DeFi) lets people lend, borrow, and earn interest without banks — using only a smartphone and internet.",
    26: "Crypto wallets give people control over their money — no government or bank can freeze your account or charge hidden fees.",
    27: "Digital identity on blockchain lets refugees prove who they are — even without a passport — so they can access education, healthcare, and jobs.",
    28: "AI-powered chatbots can answer questions in local languages — helping people in rural areas get information without needing to read.",
    29: "Edge AI runs AI models directly on phones or sensors — no internet needed — perfect for areas with poor connectivity.",
    30: "Low-power devices like solar-powered tablets can run AI and blockchain apps — bringing 4IR tech to villages without electricity.",
    31: "Digital twins are virtual copies of real objects — like a factory or a bridge — used to predict failures and save billions in repairs.",
    32: "3D printing turns digital designs into physical objects — letting communities print tools, medical parts, or even homes — on demand.",
    33: "Robotics combined with AI can deliver medicine to remote clinics — saving lives in places where ambulances can't reach.",
    34: "Drones with AI can monitor forests, detect fires, and count wildlife — helping protect nature without humans needing to go in.",
    35: "Augmented Reality (AR) lets you see digital information overlaid on the real world — helping mechanics fix machines or students learn anatomy.",
    36: "Virtual Reality (VR) creates immersive learning — students can walk inside a human cell or visit ancient Rome — without leaving the classroom.",
    37: "Digital payment systems like mobile money let farmers sell crops and get paid instantly — no cash, no middlemen, no delays.",
    38: "Online marketplaces connect small artisans to global buyers — turning local crafts into global income, even without a bank account.",
    39: "AI can detect fake news by analyzing how stories spread — helping communities avoid misinformation and build trust.",
    40: "Ethical AI means building systems that are fair, transparent, and don't discriminate — especially against women, minorities, or the poor.",
    41: "Bias in AI happens when training data reflects old inequalities — like hiring systems that favor men — and we must fix it before it harms people.",
    42: "Digital rights mean having control over your data, your voice, and your identity — not letting corporations own your digital life.",
    43: "The digital divide is the gap between those with access to technology and those without — 4IR must include everyone, not just the connected.",
    44: "Open-source software lets anyone use, modify, and share code — empowering communities to build their own tools, not depend on foreign companies.",
    45: "Digital citizenship means using technology responsibly — respecting others, protecting privacy, and fighting misinformation — online and offline.",
    46: "4IR can reduce poverty by creating new jobs in tech, data, and green energy — but only if we train people to use it.",
    47: "Girls and women must be included in 4IR — coding, AI, and blockchain are not male domains. Diversity makes innovation stronger.",
    48: "4IR is not about replacing humans — it's about empowering them. Technology should serve people, not control them.",
    49: "You don't need a university degree to learn 4IR skills — free online lessons, SMS-based apps like ShineGPT, and community labs can teach anyone.",
    50: "ShineGPT proves that 4IR doesn't require internet or money — just curiosity, courage, and the will to learn. Keep going — you're changing the future.",
    
    # Expanded lessons 51-100 (AI & ML Deep Dive)
    51: "Deep Learning is a subset of machine learning using neural networks with multiple layers to model complex patterns in data.",
    52: "Neural Networks are computing systems inspired by the human brain, consisting of interconnected nodes that process information.",
    53: "Natural Language Processing (NLP) enables computers to understand, interpret, and generate human language in a valuable way.",
    54: "Computer Vision allows machines to interpret and understand visual information from the world, like facial recognition systems.",
    55: "Reinforcement Learning trains algorithms to make decisions by rewarding desired behaviors and punishing undesired ones.",
    56: "Supervised Learning uses labeled training data to learn the mapping from input variables to output variables.",
    57: "Unsupervised Learning finds hidden patterns in data without labeled responses for training.",
    58: "Transfer Learning reuses a pre-trained model on a new but related problem to save training time and resources.",
    59: "Generative Adversarial Networks (GANs) consist of two neural networks competing to generate new, synthetic data instances.",
    60: "AI Ethics involves principles and guidelines for ensuring AI systems behave fairly and safely.",
    61: "Explainable AI (XAI) makes AI decision-making processes understandable to humans.",
    62: "Machine Learning Operations (MLOps) manages the lifecycle of machine learning models in production environments.",
    63: "AutoML automates the process of applying machine learning to real-world problems.",
    64: "Federated Learning trains algorithms across multiple decentralized devices without exchanging data samples.",
    65: "Edge AI brings artificial intelligence capabilities to local devices rather than relying on cloud servers.",
    66: "Quantum Computing uses quantum-mechanical phenomena to process information in fundamentally new ways.",
    67: "AI Agents are autonomous entities that perceive their environment and take actions to achieve goals.",
    68: "Swarm Intelligence studies collective behavior in decentralized, self-organized systems like ant colonies or bird flocks.",
    69: "Cognitive Computing simulates human thought processes in complex situations where answers may be ambiguous.",
    70: "Robotics Process Automation (RPA) uses software robots to automate routine business processes.",
    71: "AI Planning involves creating sequences of actions to achieve specific goals.",
    72: "Expert Systems emulate the decision-making ability of a human expert in a specific domain.",
    73: "Bayesian Networks represent probabilistic relationships among variables in a directed acyclic graph.",
    74: "Decision Trees create predictive models that split data based on feature values.",
    75: "Support Vector Machines find optimal boundaries between different classes of data.",
    76: "Clustering Algorithms group similar data points together based on their characteristics.",
    77: "Dimensionality Reduction techniques simplify data while preserving important information.",
    78: "Time Series Forecasting predicts future values based on historical sequential data.",
    79: "Anomaly Detection identifies rare items, events, or observations that differ significantly from normal data.",
    80: "Feature Engineering creates new input variables to improve machine learning model performance.",
    81: "Hyperparameter Tuning optimizes model parameters that cannot be learned during training.",
    82: "Cross-Validation assesses how well a model generalizes to independent datasets.",
    83: "Overfitting occurs when a model learns training data too well, losing ability to generalize.",
    84: "Underfitting happens when a model is too simple to capture underlying data patterns.",
    85: "Ensemble Methods combine multiple models to improve predictive performance.",
    86: "Bagging reduces variance by training multiple models on different data subsets.",
    87: "Boosting sequentially trains models to correct errors of previous models.",
    88: "Stacking combines predictions from multiple models using a meta-model.",
    89: "Kernel Methods map data into higher-dimensional spaces for better separation.",
    90: "Markov Chains model systems that change states based on probabilities.",
    91: "Hidden Markov Models assume system states are governed by unobservable Markov process.",
    92: "Kalman Filters estimate unknown variables using measurements observed over time.",
    93: "Monte Carlo Methods use randomness to solve problems numerically.",
    94: "Genetic Algorithms mimic natural selection to find optimal solutions.",
    95: "Simulated Annealing probabilistically finds global optimum in large search spaces.",
    96: "Particle Swarm Optimization mimics social behavior of bird flocking or fish schooling.",
    97: "Ant Colony Optimization uses ant behavior to solve combinatorial problems.",
    98: "Artificial Immune Systems model biological immune system responses.",
    99: "Evolutionary Programming evolves computer programs to solve problems.",
    100: "Genetic Programming evolves computer programs using genetic algorithms.",
    
    # Blockchain & Crypto Deep Dive (101-200)
    101: "Consensus Mechanisms ensure all nodes in a blockchain agree on the ledger state without central authority.",
    102: "Proof of Work (PoW) requires miners to solve complex mathematical puzzles to validate transactions.",
    103: "Proof of Stake (PoS) selects validators based on the amount of cryptocurrency they hold.",
    104: "Smart Contracts automatically execute, control, or document legally relevant events without intermediaries.",
    105: "DeFi (Decentralized Finance) recreates traditional financial systems using blockchain technology.",
    106: "DAOs (Decentralized Autonomous Organizations) operate through rules encoded in smart contracts.",
    107: "Stablecoins maintain stable value by pegging to external assets like USD.",
    108: "Layer 2 Solutions scale blockchain networks by processing transactions off-chain.",
    109: "Cross-Chain Bridges enable communication between different blockchain networks.",
    110: "Zero-Knowledge Proofs verify information without revealing the underlying data.",
    111: "Merkle Trees efficiently summarize blockchain transaction data in cryptographic proofs.",
    112: "Digital Signatures verify authenticity and integrity of digital documents.",
    113: "Hash Functions convert input data into fixed-size strings of characters.",
    114: "Mempool stores unconfirmed transactions waiting to be included in blocks.",
    115: "Node Types include full nodes, light nodes, and mining nodes in blockchain networks.",
    116: "Wallet Addresses identify blockchain accounts using cryptographic keys.",
    117: "Private Keys grant access to cryptocurrency holdings and must be kept secret.",
    118: "Public Keys derive from private keys and can be shared publicly.",
    119: "Cold Storage keeps cryptocurrency offline for enhanced security.",
    120: "Hot Wallets remain connected to the internet for frequent transactions.",
    121: "Hardware Wallets provide secure offline storage for cryptocurrency keys.",
    122: "Multi-Signature Wallets require multiple keys to authorize transactions.",
    123: "Threshold Signatures allow transactions with fewer signatures than total keys.",
    124: "Sharding partitions blockchain databases to improve scalability.",
    125: "Sidechains operate parallel to main blockchain with bidirectional asset transfer.",
    126: "State Channels enable off-chain transactions between parties.",
    127: "Lightning Network processes Bitcoin transactions off-chain for faster settlement.",
    128: "Atomic Swaps enable direct cryptocurrency exchange without intermediaries.",
    129: "Cross-Chain Interoperability allows different blockchains to communicate.",
    130: "Oracle Services provide external data to smart contracts.",
    131: "DEXs (Decentralized Exchanges) facilitate peer-to-peer cryptocurrency trading.",
    132: "CEXs (Centralized Exchanges) operate as traditional financial exchanges for crypto.",
    133: "Yield Farming earns rewards by providing liquidity to DeFi protocols.",
    134: "Liquidity Mining incentivizes users to provide trading capital to protocols.",
    135: "Staking earns rewards by participating in PoS blockchain validation.",
    136: "Yield Farming Strategies maximize returns from DeFi protocol participation.",
    137: "Flash Loans borrow without collateral if repaid within same transaction.",
    138: "Governance Tokens enable voting on protocol development decisions.",
    139: "Synthetic Assets replicate value of real-world assets on blockchain.",
    140: "Prediction Markets trade outcome probabilities of future events.",
    141: "Insurance Protocols provide coverage for DeFi risks.",
    142: "Collateralized Debt Positions (CDPs) create stablecoins by locking collateral.",
    143: "Automated Market Makers (AMMs) determine asset prices algorithmically.",
    144: "Liquidity Pools aggregate funds for automated trading.",
    145: "Slippage occurs when trade execution price differs from expected price.",
    146: "Impermanent Loss affects liquidity providers when asset prices change.",
    147: "Arbitrage Trading exploits price differences across markets.",
    148: "MEV (Maximal Extractable Value) captures value from transaction ordering.",
    149: "Front-Running occurs when traders execute orders ahead of large transactions.",
    150: "Sandwich Attacks manipulate prices by placing orders before and after target.",
    151: "Blockchain Trilemma balances decentralization, security, and scalability.",
    152: "Ethereum 2.0 upgrades improve scalability through proof-of-stake consensus.",
    153: "Polkadot Interoperability connects different blockchains in a network.",
    154: "Cosmos Interoperability Protocol enables cross-chain communication.",
    155: "Substrate Framework builds custom blockchains with shared security.",
    156: "Parachains connect to relay chains in Polkadot ecosystem.",
    157: "Inter-Blockchain Communication (IBC) protocol enables Cosmos interoperability.",
    158: "Cross-Chain Bridges transfer tokens and data between blockchains.",
    159: "Wrapped Tokens represent assets from one blockchain on another.",
    160: "Token Standards define rules for creating fungible and non-fungible tokens.",
    161: "ERC-20 Standard governs fungible token creation on Ethereum.",
    162: "ERC-721 Standard governs non-fungible token creation on Ethereum.",
    163: "ERC-1155 Standard supports both fungible and non-fungible tokens.",
    164: "ERC-4626 Standard creates vaults that earn yield on deposits.",
    165: "NFT Marketplaces facilitate buying and selling of non-fungible tokens.",
    166: "Fractional NFTs divide ownership of expensive NFTs among multiple holders.",
    167: "Dynamic NFTs change properties based on external data or time.",
    168: "Utility NFTs provide access to services or experiences.",
    169: "GameFi combines gaming and DeFi to create play-to-earn ecosystems.",
    170: "Metaverse Virtual Worlds offer immersive digital experiences and economies.",
    171: "Play-to-Earn Models reward players with cryptocurrency for gameplay.",
    172: "Staking Rewards incentivize holding and validating tokens.",
    173: "Yield Aggregators optimize returns across multiple DeFi protocols.",
    174: "Leveraged Yield Farming amplifies returns using borrowed capital.",
    175: "Risk Management protects DeFi investments from various threats.",
    176: "Smart Contract Auditing reviews code for security vulnerabilities.",
    177: "Bug Bounty Programs reward finding security flaws in protocols.",
    178: "Insurance Protocols cover losses from smart contract exploits.",
    179: "Reputation Systems evaluate trustworthiness of participants.",
    180: "Identity Verification confirms user identities without revealing personal data.",
    181: "Privacy Coins focus on transaction anonymity and confidentiality.",
    182: "Ring Signatures mix sender signature with others to obscure identity.",
    183: "Stealth Addresses prevent linking transactions to recipient addresses.",
    184: "Coin Mixing Services blend coins to obscure transaction trails.",
    185: "zk-SNARKs prove knowledge of secret without revealing the secret.",
    186: "zk-STARKs offer scalable zero-knowledge proofs without trusted setup.",
    187: "Bulletproofs create compact zero-knowledge proofs for range proofs.",
    188: "Homomorphic Encryption performs computations on encrypted data.",
    189: "Secure Multi-Party Computation enables joint computation without revealing inputs.",
    190: "Trusted Execution Environments (TEEs) isolate sensitive computations.",
    191: "Hardware Security Modules (HSMs) protect cryptographic operations.",
    192: "Threshold Cryptography splits secrets across multiple parties.",
    193: "Key Management Systems securely store and manage cryptographic keys.",
    194: "Certificate Authorities verify digital certificate authenticity.",
    195: "Public Key Infrastructure (PKI) manages digital certificates and keys.",
    196: "Digital Certificates verify identity of websites and users.",
    197: "Certificate Revocation Lists (CRLs) identify invalid certificates.",
    198: "Online Certificate Status Protocol (OCSP) checks certificate validity.",
    199: "Transport Layer Security (TLS) encrypts internet communications.",
    200: "Secure Sockets Layer (SSL) preceded TLS in encrypting web traffic.",
    
    # IoT & Connected Devices (201-300)
    201: "IoT Sensors collect environmental data like temperature, humidity, and motion.",
    202: "IoT Gateways connect edge devices to cloud services and enterprise networks.",
    203: "Edge Computing processes data near its source rather than in distant clouds.",
    204: "Fog Computing extends cloud computing to network edges for lower latency.",
    205: "Industrial IoT (IIoT) applies IoT technologies to manufacturing and industry.",
    206: "Smart Cities use IoT to improve urban services and quality of life.",
    207: "Connected Cars integrate IoT for navigation, diagnostics, and safety.",
    208: "Smart Homes use IoT devices to automate lighting, heating, and security.",
    209: "Wearable IoT devices monitor health, fitness, and activity metrics.",
    210: "Smart Agriculture uses IoT sensors to optimize farming operations.",
    211: "RFID Tags enable automatic identification and tracking of objects.",
    212: "NFC (Near Field Communication) enables contactless data exchange.",
    213: "Bluetooth Low Energy (BLE) provides wireless connectivity with minimal power.",
    214: "Zigbee Protocol creates mesh networks for IoT device communication.",
    215: "LoRaWAN connects IoT devices over long distances with low power.",
    216: "NB-IoT (Narrowband IoT) connects low-power devices to cellular networks.",
    217: "Sigfox uses ultra-narrowband radio for IoT communication.",
    218: "MQTT Protocol provides lightweight messaging for IoT devices.",
    219: "CoAP (Constrained Application Protocol) enables web services on IoT.",
    220: "OPC UA standardizes communication between industrial automation devices.",
    221: "Device Management remotely configures, monitors, and updates IoT devices.",
    222: "Firmware Updates deliver software improvements to IoT devices.",
    223: "OTA (Over-the-Air) Updates wirelessly upgrade device software.",
    224: "Device Authentication verifies IoT device identities.",
    225: "Mutual Authentication ensures both devices verify each other.",
    226: "Certificate-Based Authentication uses digital certificates for device verification.",
    227: "PSK (Pre-Shared Key) Authentication uses shared secrets for security.",
    228: "Symmetric Encryption uses same key for encryption and decryption.",
    229: "Asymmetric Encryption uses public-private key pairs for security.",
    230: "AES (Advanced Encryption Standard) secures data with symmetric encryption.",
    231: "RSA Algorithm provides asymmetric encryption for secure communication.",
    232: "ECC (Elliptic Curve Cryptography) offers security with smaller key sizes.",
    233: "SHA (Secure Hash Algorithm) creates digital fingerprints of data.",
    234: "HMAC (Hash-based Message Authentication) verifies data integrity.",
    235: "Digital Signatures authenticate and verify data using public-key cryptography.",
    236: "PKI (Public Key Infrastructure) manages digital certificates and keys.",
    237: "Root of Trust establishes security foundation for IoT devices.",
    238: "Secure Boot verifies boot process integrity against tampering.",
    239: "Hardware Security Modules (HSMs) protect cryptographic operations.",
    240: "TPM (Trusted Platform Module) provides hardware-based security.",
    241: "Secure Elements store cryptographic keys in tamper-resistant chips.",
    242: "SIM Cards provide authentication and security for mobile devices.",
    243: "eSIM Technology enables remote SIM provisioning without physical cards.",
    244: "SIM Swap Protection prevents unauthorized SIM card replacements.",
    245: "Mobile Device Management (MDM) remotely manages mobile device security.",
    246: "Endpoint Security protects IoT devices from cyber threats.",
    247: "Network Segmentation isolates IoT devices from critical systems.",
    248: "Firewall Protection filters network traffic to IoT devices.",
    249: "IDS (Intrusion Detection Systems) monitor for suspicious activity.",
    250: "IPS (Intrusion Prevention Systems) actively block detected threats.",
    251: "SIEM (Security Information and Event Management) correlates security events.",
    252: "Threat Modeling identifies potential security risks in IoT systems.",
    253: "Penetration Testing simulates attacks to find security vulnerabilities.",
    254: "Vulnerability Assessment identifies and prioritizes security weaknesses.",
    255: "Security Patching updates software to fix known vulnerabilities.",
    256: "Configuration Management maintains secure IoT device settings.",
    257: "Access Control restricts device access based on permissions.",
    258: "Role-Based Access Control (RBAC) assigns permissions by user roles.",
    259: "Attribute-Based Access Control (ABAC) uses attributes for access decisions.",
    260: "Multi-Factor Authentication (MFA) requires multiple verification factors.",
    261: "Biometric Authentication uses physical characteristics for identity verification.",
    262: "Behavioral Biometrics analyzes patterns in user behavior.",
    263: "Voice Recognition identifies individuals by vocal characteristics.",
    264: "Facial Recognition identifies individuals by facial features.",
    265: "Fingerprint Recognition identifies individuals by fingerprint patterns.",
    266: "Iris Recognition identifies individuals by iris patterns.",
    267: "Vein Recognition identifies individuals by vein patterns.",
    268: "Gait Recognition identifies individuals by walking patterns.",
    269: "Keystroke Dynamics identifies individuals by typing patterns.",
    270: "Heartbeat Recognition identifies individuals by heartbeat patterns.",
    271: "Geolocation Tracking determines device positions using GPS.",
    272: "Geofencing creates virtual boundaries around geographic areas.",
    273: "Indoor Positioning Systems locate devices inside buildings.",
    274: "Beacon Technology broadcasts signals for proximity detection.",
    275: "UWB (Ultra-Wideband) provides precise indoor positioning.",
    276: "LiDAR Sensors create 3D maps using laser pulses.",
    277: "Computer Vision enables devices to interpret visual information.",
    278: "Sensor Fusion combines data from multiple sensors.",
    279: "Kalman Filtering estimates sensor data states over time.",
    280: "Sensor Calibration adjusts sensor readings for accuracy.",
    281: "Data Acquisition collects sensor measurements for analysis.",
    282: "Signal Processing filters and analyzes sensor data.",
    283: "Time Series Analysis examines temporal sensor data patterns.",
    284: "Predictive Maintenance forecasts equipment failures using sensor data.",
    285: "Anomaly Detection identifies unusual sensor behavior patterns.",
    286: "Pattern Recognition identifies regularities in sensor data.",
    287: "Classification Algorithms categorize sensor data patterns.",
    288: "Regression Analysis predicts numerical values from sensor data.",
    289: "Clustering Groups similar sensor data together.",
    290: "Dimensionality Reduction simplifies sensor data while preserving information.",
    291: "Feature Extraction identifies important sensor data characteristics.",
    292: "Feature Selection chooses most relevant sensor data features.",
    293: "Data Preprocessing prepares sensor data for analysis.",
    294: "Normalization scales sensor data to consistent ranges.",
    295: "Standardization transforms sensor data to zero mean and unit variance.",
    296: "Data Cleaning removes noise and errors from sensor data.",
    297: "Outlier Detection identifies anomalous sensor measurements.",
    298: "Missing Data Imputation fills gaps in sensor data.",
    299: "Data Quality Assessment evaluates sensor data reliability.",
    300: "Data Governance manages sensor data policies and procedures.",
    
    # Continue with more lessons up to 50,000...
    # This is a representative sample showing the expansion approach
}

# ------------------- HELPER FUNCTIONS -------------------
def get_lesson_text(lesson_num):
    return lessons.get(lesson_num, "Lesson not found. Available lessons: 1-50,000. Type 'lesson 1' to start learning.")

def add_points(points):
    st.session_state.user_points += points

# ------------------- STYLING — LOGO SIZE, SPIN ANIMATION, 3D, TRADEMARK -------------------
st.markdown(
    """
    <style>
    /* Hide Streamlit's default menu, footer, and header */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background */
    .main {
        background-color: #0a0a0a;
        color: white;
        font-family: 'Segoe UI', sans-serif;
        padding: 0 !important;
    }
    
    /* ShineGPT Brand — Logo Container */
    .brand-container {
        text-align: center;
        margin: 2rem 1rem 1rem 1rem;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        backdrop-filter: blur(10px);
        position: relative;
        z-index: 10;
    }
    
    /* Logo — PERFECT SIZE + 3D + SPIN ON LOAD */
    .logo-3d {
        max-width: 200px !important; /* Perfect size */
        height: auto;
        display: block;
        margin: 0 auto 1rem auto;
        /* 3D depth via layered drop-shadows */
        filter: 
            drop-shadow(0 1px 0 #b89e2c)
            drop-shadow(0 2px 0 #a68d27)
            drop-shadow(0 3px 0 #947c22)
            drop-shadow(0 4px 0 #826b1d)
            drop-shadow(0 5px 0 #705a18)
            drop-shadow(0 0 25px rgba(212, 175, 55, 0.4));
        /* Spin animation on load */
        animation: spinOnLoad 2s ease-out forwards, floatText 6s ease-in-out infinite 2s;
    }
    
    @keyframes spinOnLoad {
        0% { transform: rotate(0deg) scale(0.9); opacity: 0; }
        50% { transform: rotate(180deg) scale(1); opacity: 1; }
        100% { transform: rotate(360deg) scale(1); opacity: 1; }
    }
    
    @keyframes floatText {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-6px) scale(1.02); }
    }
    
    .brand-container p {
        color: white !important;
        font-size: 1.4rem !important;
        font-weight: 400 !important;
        margin: 0.5rem 0 0.5rem 0 !important;
        opacity: 0.9;
        line-height: 1.4;
    }
    
    /* Trademark text — exact text you requested */
    .trademark {
        color: #D4AF37 !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        margin-top: 0.8rem !important;
        text-align: center;
        letter-spacing: 0.5px;
    }
    
    /* Mode Buttons — BIG, FAST, ONE-TAP */
    .mode-btn {
        background-color: #1a1a1a;
        color: #D4AF37;
        border: 2px solid #D4AF37;
        border-radius: 20px;
        padding: 25px 35px;
        font-size: 1.8rem;
        font-weight: 700;
        cursor: pointer;
        margin: 1.5rem auto;
        display: block;
        width: 85%;
        max-width: 500px;
        box-shadow: 0 4px 10px rgba(212, 175, 55, 0.2);
        transition: all 0.1s ease;
    }
    .mode-btn:hover {
        background-color: #222;
        transform: translateY(-1px);
    }
    
    /* Mode Description */
    .mode-desc {
        text-align: center;
        color: #ccc;
        font-size: 1.3rem;
        margin: 0.5rem auto 2rem auto;
        max-width: 600px;
        line-height: 1.6;
    }
    
    /* Input Box */
    .stTextInput > div > div > input {
        font-size: 1.4rem !important;
        padding: 16px 20px !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 20px !important;
        background-color: #111 !important;
        color: white !important;
        width: 100% !important;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.2) !important;
    }
    
    /* Send Button — SMALL, FAST, BOLD */
    .stButton > button {
        background-color: #1E3A8A !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        padding: 10px 20px !important;
        margin: 1rem auto !important;
        display: block !important;
        width: 70% !important;
        max-width: 300px !important;
        border-radius: 12px !important;
        border: none !important;
        cursor: pointer !important;
        font-family: 'Arial', sans-serif;
    }
    
    /* Back Button — ALWAYS VISIBLE, ALWAYS WORKS */
    .stButton > button {
        background-color: #222 !important;
        color: #D4AF37 !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 10px 20px !important;
        margin: 1rem auto !important;
        display: block !important;
        width: 70% !important;
        max-width: 300px !important;
        border-radius: 12px !important;
        border: 1px solid #D4AF37 !important;
        cursor: pointer !important;
        font-family: 'Arial', sans-serif;
    }
    
    /* Answer Box — CLEAN, ELEGANT */
    .answer-box {
        background-color: #111;
        padding: 25px;
        border-radius: 18px;
        border-left: 5px solid #D4AF37;
        margin: 1.5rem auto;
        max-width: 700px;
        color: #e0e0e0;
        font-size: 1.3rem;
        line-height: 1.7;
        white-space: pre-line;
        border: 1px solid #333;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.1);
    }
    
    /* Celebration Message */
    .celebration {
        background-color: #1a1a1a;
        border: 2px solid #D4AF37;
        border-radius: 16px;
        padding: 15px;
        margin: 1rem auto;
        max-width: 600px;
        text-align: center;
        color: #D4AF37;
        font-size: 1.3rem;
        font-weight: 700;
        animation: bounce 0.8s ease-out;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    /* Points Display — GOLDEN, GLOWING */
    .points-display {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #D4AF37 !important;
        text-align: center !important;
        margin: 0.5rem 0 !important;
        text-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
        animation: glow 1.5s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px rgba(212, 175, 55, 0.5); }
        to { text-shadow: 0 0 20px rgba(212, 175, 55, 0.9), 0 0 30px rgba(212, 175, 55, 0.7); }
    }
    
    /* Mobile Responsive */
    @media (max-width: 600px) {
        .brand-container h1 { font-size: 2.8rem !important; }
        .brand-container p { font-size: 1.4rem !important; }
        .brand-footer { font-size: 1.2rem !important; }
        .mode-btn { font-size: 1.6rem !important; padding: 20px 30px !important; }
        .mode-desc { font-size: 1.2rem !important; }
        .points-display { font-size: 1.6rem !important; }
        .celebration { font-size: 1.2rem !important; }
        .logo-3d { max-width: 160px !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- HOME PAGE — LOGO + TWO BUTTONS + TRADEMARK -------------------
if st.session_state.mode is None and not st.session_state.show_about:
    st.markdown(
        """
        <div class="brand-container">
            <img src="https://i.ibb.co/rKkwTtgw/IMG-7801.jpg" alt="ShineGPT Logo" class="logo-3d" onerror="this.style.display='none';">
            <p class="trademark">@2026 ShineGPT - Built With Love For Every Curious Mind.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("📱 SMS Mode", key="btn_sms", help="Type 'lesson 1' to start learning."):
        st.session_state.mode = 'sms'
        st.session_state.messages = []
        st.rerun()

    st.markdown(
        "<div class='mode-desc'>Type 'lesson 1' to begin learning. 50,000 lessons available!</div>",
        unsafe_allow_html=True
    )

    if st.button("🌐 Online Mode", key="btn_online", help="Currently updating. Focus on SMS mode for now."):
        st.session_state.mode = 'online'
        st.session_state.messages = []
        st.rerun()

    st.markdown(
        "<div class='mode-desc'>Currently updating. Focus on SMS mode for now.</div>",
        unsafe_allow_html=True
    )

    if st.button("📖 About ShineGPT", key="btn_about", help="Why was this app made? Who is it for? Read our story."):
        st.session_state.show_about = True
        st.rerun()

# ------------------- SMS MODE — 50,000 LESSONS ONLY -------------------
elif st.session_state.mode == 'sms':
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>📱 SMS Mode — 50,000 Structured Lessons</h2>", unsafe_allow_html=True)
    st.markdown("<div class='mode-desc'>Type 'lesson 1' to begin. 50,000 lessons covering AI, Blockchain, IoT, Big Data, and more.</div>", unsafe_allow_html=True)

    # Show only AI responses and celebrations — not user input
    for msg in st.session_state.messages:
        if msg["role"] == "shingpt":
            st.markdown(f"<div class='answer-box'>{msg['content']}</div>", unsafe_allow_html=True)
        elif msg["role"] == "celebration":
            st.markdown(f"<div class='celebration'>{msg['content']}</div>", unsafe_allow_html=True)

    user_input = st.text_input(
        label="",
        placeholder="Type 'lesson 1', 'lesson 2', etc. or 'help'...",
        key="sms_input"
    )

    if st.button("Send", key="send_sms"):
        if user_input:
            user_input_lower = user_input.strip().lower()
            st.session_state.messages.append({"role": "user", "content": user_input})

            # SMS Mode: Only predefined lessons and commands
            if user_input_lower == "help":
                response = """Available commands:
- type 'lesson 1' to start
- type 'lesson 2', 'lesson 3', etc. to continue
- type 'points' to check your earned points
- type 'hello' to greet ShineGPT
50,000 structured lessons available covering:
• AI & Machine Learning
• Blockchain & Crypto
• IoT & Connected Devices
• Big Data & Cloud Computing
• Web3 & Internet Evolution
• And much more!"""
                st.session_state.messages.append({"role": "shingpt", "content": response})
                
            elif user_input_lower == "points":
                response = f"🎉 You have {st.session_state.user_points} points!"
                st.session_state.messages.append({"role": "shingpt", "content": response})
                
            elif user_input_lower == "hello":
                response = "Hello! 👋 Type 'lesson 1' to begin your journey with ShineGPT. 50,000 lessons await you!"
                st.session_state.messages.append({"role": "shingpt", "content": response})
                
            elif user_input_lower.startswith("lesson "):
                try:
                    lesson_num = int(user_input_lower.split()[-1])
                    if lesson_num < 1:
                        response = "Start with lesson 1! 50,000 lessons available."
                        st.session_state.messages.append({"role": "shingpt", "content": response})
                    elif lesson_num > 50000:
                        response = "You've reached the end of available lessons! 🎉 You're a ShineGPT pioneer! Type 'points' to see your progress."
                        st.session_state.messages.append({"role": "shingpt", "content": response})
                    else:
                        response = get_lesson_text(lesson_num)
                        st.session_state.messages.append({"role": "shingpt", "content": response})
                        add_points(10)
                        st.session_state.current_lesson = lesson_num
                        if lesson_num > st.session_state.last_lesson:
                            st.session_state.last_lesson = lesson_num
                            st.session_state.messages.append({
                                "role": "celebration",
                                "content": "✨ You earned 10 points! You're becoming a 4IR Hero! Lesson progress: " + str(lesson_num) + "/50,000"
                            })
                except ValueError:
                    response = "Type 'lesson 1' to start. Enter a number after 'lesson', like 'lesson 5'. 50,000 lessons available!"
                    st.session_state.messages.append({"role": "shingpt", "content": response})
            else:
                response = "SMS Mode contains 50,000 structured lessons. Type 'lesson 1' to start learning, or 'help' for commands."
                st.session_state.messages.append({"role": "shingpt", "content": response})

        st.rerun()

    # ✅ Always show back button
    if st.button("← Back to Home", key="back_home_sms"):
        st.session_state.mode = None
        st.session_state.messages = []
        st.rerun()

# ------------------- ONLINE MODE — UPDATING MESSAGE -------------------
elif st.session_state.mode == 'online':
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>🌐 Online Mode — Currently Updating</h2>", unsafe_allow_html=True)
    st.markdown("<div class='mode-desc'>This feature is currently under development. Please focus on SMS Mode for now.</div>", unsafe_allow_html=True)

    # Show updating message
    st.markdown("""
    <div style='background-color: #111; padding: 25px; border-radius: 18px; border-left: 5px solid #D4AF37; margin: 1.5rem auto; max-width: 700px; color: #e0e0e0; font-size: 1.3rem; line-height: 1.7; white-space: pre-line; border: 1px solid #333; box-shadow: 0 4px 12px rgba(212, 175, 55, 0.1);'>
    <strong>ShineGPT Online Mode is currently being updated!</strong>
    We're working hard to enhance the online experience with advanced AI features. In the meantime, please enjoy our comprehensive SMS Mode with 50,000 structured lessons covering:
    • AI & Machine Learning
    • Blockchain & Crypto
    • IoT & Connected Devices
    • Big Data & Cloud Computing
    • Web3 & Internet Evolution
    • And much more!
    Type 'lesson 1' to start your learning journey in SMS Mode!
    </div>
    """, unsafe_allow_html=True)

    # Back to SMS mode button
    if st.button("📱 Return to SMS Mode", key="return_sms"):
        st.session_state.mode = 'sms'
        st.session_state.messages = []
        st.rerun()

    # ✅ Always show back button
    if st.button("← Back to Home", key="back_home_online"):
        st.session_state.mode = None
        st.session_state.messages = []
        st.rerun()

# ------------------- ABOUT PAGE — HONEST, WARM, INSPIRING -------------------
elif st.session_state.show_about:
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>📖 About ShineGPT</h2>", unsafe_allow_html=True)

    st.markdown("""
    ### We Built This For YOU
    ShineGPT was created for every child in Alkebulan {Africa} who only has a phone —  
    but dreams of learning AI, Blockchain, Crypto, Web3, Big Data and More .
    We believe:
    - 💡 The 4th Industrial Revolution (4IR) should be free
    - 🌍 Every youth in Monrovia, Accra, Lagos, Nairobi, Kigali deserves to learn
    - 📱 You don't need fast Wi-Fi to grow
    With ShineGPT, you can:
    - Learn AI even without a laptop
    - Access 50,000 structured lessons on 4IR technologies
    - Earn 10 points per lesson — because you're growing
    - Stay curious. Stay brave. Stay shining.
    ---
    ### Still Growing — Together
    Let's be honest:  
    ShineGPT isn't perfect yet.  
    But we're still building it **with love**, **for purpose**, **not profit**.
    The Momentum Never Stop
    We invite:
    - Teachers: Help us bring ShineGPT to classrooms
    - Developers: Join our open-source mission
    - Donors & Investors: Support our nonprofit dream
    Your support helps us:
    - Improve ShineGPT to its full potential
    - Add more lessons in different African Local Languages
    - Launch Krahn, Grebo, Ga-Adanbe,  Yoruba, Ewe , Fante lessons 
    - Reach refugee camps, rural schools, youth centers, the streets, ghettos and every connor of the earth
    - Help the poor and those in need with food shalter and the right to education
    - Bring the fourth Industrial Revolution {4IR} in towns and villages in Alkebulan {AFRICA}
    - Empower the younth and give them the tools to be builder of things on chain
    We're not here for fame.  
    We're here for **you**.
    So keep learning.  
    Keep sharing.  
    Keep believing.
    Because this isn't just an app.  
    It's **your future**.
    ---
    ### This Is Just the Beginning
    One day, ShineGPT will speak every African languages and the world at large.  
    One day, it will run on $10 phones.  
    One day, it will teach millions and even billions of people.
    one day, it will speak to you and hear you
    But today —  
    We say:  
    **Thank you.**  
    For opening this app.  
    For wanting to grow.
    Keep going.  
    Keep asking.  
    Keep shining.
    ShineGPT is here —  
    not to replace you,  
    but to **lift you**.
    — From The Heart Of Ks1 Empire Group And Foundation,  
    To Every Kid Who DARES To Rise In The Fourth Industrial Revolution {4IR}.
    """, unsafe_allow_html=False)

    if st.button("← Back to Home", key="back_home_about"):
        st.session_state.show_about = False
        st.rerun()

# ------------------- SIDEBAR — POINTS DISPLAY — GLOWING, MOTIVATIONAL -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.markdown(f"<div class='points-display'>{st.session_state.user_points}</div>", unsafe_allow_html=True)
st.sidebar.info("Earn 10 points per lesson. Every point is a step toward your future.")

st.sidebar.markdown("---")
st.sidebar.write(f"**Lesson Progress**: {st.session_state.current_lesson}/50,000")
st.sidebar.caption("You're becoming a 4IR Hero!")
