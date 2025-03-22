# do_gfg

## Overview  
`do_gfg` is an automation tool that logs into **GeeksforGeeks (GFG)**, solves the **Problem of the Day**, and posts the solution on **X (formerly Twitter)**.

## Setup Instructions  

### 1. Prerequisites  
Ensure you have the following installed on your system:  

- **Python 3.8+**  
- **Google Chrome** (or another browser compatible with Selenium)  
- **ChromeDriver** (matching your Chrome version)  

### 2. Clone the Repository  
```sh
git clone https://github.com/yourusername/do_gfg.git
cd do_gfg
```

### 3. Create a Virtual Environment (Optional but Recommended)  
```sh
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### 4. Install Dependencies  
```sh
pip install -r requirements.txt
```


```ini
X_GMAIL=your-email@example.com
X_USERNAME=your-username
X_PASSWORD=your-password
GFG_EMAIL=your-gfg-email
GFG_PASSWORD=your-gfg-password
```

Alternatively, you can set them in the terminal:  

#### For Mac/Linux  
```sh
export X_GMAIL="your-email@example.com"
export X_USERNAME="your-username"
export X_PASSWORD="your-password"
export GFG_EMAIL="your-gfg-email"
export GFG_PASSWORD="your-gfg-password"
```

#### For Windows (CMD)  
```sh
set X_GMAIL=your-email@example.com
set X_USERNAME=your-username
set X_PASSWORD=your-password
set GFG_EMAIL=your-gfg-email
set GFG_PASSWORD=your-gfg-password
```

### 6. Run the Script  
```sh
python main.py
```

## Next Steps  
- Automate GFG login  
- Solve Problem of the Day  
- Capture solution and post it on X