<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ShineGPT - Learn 4IR Technologies</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        body {
            background-color: #000;
            color: white;
            line-height: 1.6;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        /* Header */
        header {
            text-align: center;
            padding: 60px 20px;
            background: #000;
        }
        .logo {
            color: #D4AF37;
            font-size: 4rem;
            font-weight: 900;
            letter-spacing: -2px;
            margin-bottom: 10px;
        }
        .tagline {
            font-size: 1.8rem;
            color: white;
            margin-bottom: 30px;
            opacity: 0.9;
        }
        .sponsor {
            color: #1E3A8A;
            font-size: 1.4rem;
            font-weight: 700;
            opacity: 0.9;
            margin-bottom: 20px;
        }
        .description {
            color: #ccc;
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto 40px;
            line-height: 1.8;
        }
        /* Features Section */
        .features {
            padding: 80px 20px;
            text-align: center;
            background: #000;
        }
        .section-title {
            color: #1E3A8A; /* Blue color */
            font-size: 2.5rem;
            margin-bottom: 50px;
            text-align: center;
            text-shadow: 
                0 1px 0 #ccc,
                0 2px 0 #c9c9c9,
                0 3px 0 #bbb,
                0 4px 0 #b9b9b9,
                0 5px 0 #aaa,
                0 6px 1px rgba(0,0,0,.1),
                0 0 5px rgba(0,0,0,.1),
                0 1px 3px rgba(0,0,0,.3),
                0 3px 5px rgba(0,0,0,.2),
                0 5px 10px rgba(0,0,0,.25),
                0 10px 10px rgba(0,0,0,.2),
                0 20px 20px rgba(0,0,0,.15);
            letter-spacing: 1px;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            max-width: 1000px;
            margin: 0 auto;
        }
        .feature-card {
            background: #111;
            border-radius: 15px;
            padding: 30px;
            border: 1px solid #333;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 25px rgba(212, 175, 55, 0.2);
        }
        .feature-icon {
            font-size: 3rem;
            color: #D4AF37;
            margin-bottom: 20px;
        }
        .feature-title {
            color: #D4AF37;
            font-size: 1.5rem;
            margin-bottom: 15px;
        }
        .feature-desc {
            color: #ccc;
            font-size: 1.1rem;
        }
        /* How It Works */
        .how-it-works {
            padding: 80px 20px;
            background: #000;
        }
        .how-it-works .section-title {
            color: #1E3A8A; /* Blue color */
            text-shadow: 
                0 1px 0 #ccc,
                0 2px 0 #c9c9c9,
                0 3px 0 #bbb,
                0 4px 0 #b9b9b9,
                0 5px 0 #aaa,
                0 6px 1px rgba(0,0,0,.1),
                0 0 5px rgba(0,0,0,.1),
                0 1px 3px rgba(0,0,0,.3),
                0 3px 5px rgba(0,0,0,.2),
                0 5px 10px rgba(0,0,0,.25),
                0 10px 10px rgba(0,0,0,.2),
                0 20px 20px rgba(0,0,0,.15);
            letter-spacing: 1px;
        }
        .steps {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 30px;
            max-width: 1000px;
            margin: 0 auto;
        }
        .step-card {
            background: #111;
            border-radius: 15px;
            padding: 30px;
            width: 250px;
            text-align: center;
            border: 1px solid #333;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .step-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 25px rgba(212, 175, 55, 0.2);
        }
        .step-number {
            display: inline-block;
            background: #D4AF37;
            color: #0a0a0a;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            line-height: 50px;
            font-weight: bold;
            font-size: 1.5rem;
            margin-bottom: 20px;
        }
        .step-title {
            color: #D4AF37;
            font-size: 1.3rem;
            margin-bottom: 15px;
        }
        .step-desc {
            color: #ccc;
        }
        /* Launch Button */
        .launch-section {
            text-align: center;
            padding: 60px 20px;
            background: #000;
        }
        .launch-btn {
            background-color: #1E3A8A;
            color: white;
            border: none;
            padding: 20px 50px;
            font-size: 1.5rem;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 700;
            text-decoration: none;
            display: inline-block;
        }
        .launch-btn:hover {
            background-color: #2563eb;
            transform: scale(1.05);
        }
        /* Footer */
        footer {
            text-align: center;
            padding: 40px 20px;
            background: #000;
            border-top: 1px solid #333;
        }
        .copyright {
            color: #888;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container">
            <div class="logo">SHINEGPT</div>
            <div class="tagline">Learn. Earn Knowledge. Empower Yourself.</div>
            <div class="sponsor">Sponsored By The KS1 Empire Group & Foundation</div>
            <div class="description">A free, low-data-first AI tutor for Alkebulan {Africa} youth and learners in low-connectivity areas</div>
        </div>
    </header>

    <!-- Features Section -->
    <section class="features">
        <div class="container">
            <h2 class="section-title">Why ShineGPT?</h2>
            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-icon">📚</div>
                    <h3 class="feature-title">50,000 Structured Lessons</h3>
                    <p class="feature-desc">Comprehensive lessons covering AI, Blockchain, IoT, Big Data, Web3, and more. Learn at your own pace.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📱</div>
                    <h3 class="feature-title">SMS & Online Modes</h3>
                    <p class="feature-desc">Low-data SMS mode for anywhere, anytime learning. Online mode for interactive Q&A (currently updating).</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎯</div>
                    <h3 class="feature-title">4IR Focused</h3>
                    <p class="feature-desc">Specialized in Fourth Industrial Revolution technologies - AI, Blockchain, IoT, Big Data, and more.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- How It Works -->
    <section class="how-it-works">
        <div class="container">
            <h2 class="section-title">How It Works</h2>
            <div class="steps">
                <div class="step-card">
                    <div class="step-number">1</div>
                    <h3 class="step-title">Choose Mode</h3>
                    <p class="step-desc">Select SMS mode for learning, Online Mode is currently being updated. Thanks for your patience.</p>
                </div>
                <div class="step-card">
                    <div class="step-number">2</div>
                    <h3 class="step-title">Start Learning</h3>
                    <p class="step-desc">Type 'lesson 1' to begin with 50,000 structured lessons</p>
                </div>
                <div class="step-card">
                    <div class="step-number">3</div>
                    <h3 class="step-title">Earn Points</h3>
                    <p class="step-desc">Get 10 points per lesson. Track your progress as you advance</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Launch Button -->
    <section class="launch-section">
        <a href="https://huggingface.co/spaces/shinehome888/ShineGPT" target="_blank">
            <button class="launch-btn">LAUNCH SHINEGPT</button>
        </a>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <p class="copyright">@2026 ShineGPT - A nonprofit project by KS1 Empire Group & Foundation (KS1EGF)</p>
            <p class="built-with">Built with love for every curious mind</p>
        </div>
    </footer>
</body>
</html>
