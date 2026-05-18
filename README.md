# 🧮 Scientific Calculator Python

A fully functional, theme-switchable **Scientific Calculator** built using **Python's Tkinter** library.

It supports **arithmetic**, **scientific**, and **memory-based operations** with a responsive and intuitive interface.

---

## 📂 Project Structure

```bash
Scientific-Calculator-Python/
│
├── main.py                     # Main application
├── LICENSE
└── README.md                   # Project documentation
```

---

## ⚙️ Features

-   🎨 **Light/Dark Theme**
-   🧮 **Scientific Functions**: sin, cos, tan, log, sqrt, powers, etc.
-   💾 **Memory Functions**:
    -   `M+` → Add to memory
    -   `M−` → Subtract from memory
    -   `MR` → Recall memory
-   🧠 **History Log** --> Automatically saves last 10 calculations
-   ⌨️ **Keyboard Shortcuts** for fast operation
-   🧰 **Smart Input Handling** --> Auto-balances parentheses and
    sanitizes expressions
-   💥 **Error Handling** --> Prevents invalid evaluations and protects
    against code injection

---

## 🚀 How to Use

1. Clone or download the project  
   ```bash
   git clone https://github.com/sagesakshi27/Scientific-Calculator-Python.git
   ```

2. Open the project folder  
   ```bash
   cd Scientific-Calculator-Python
   ```

3. Run the project
   ```bash
   python main.py
   ```

---

## 🧠 How It Works

1.  **Input Capture:**
    Expressions are built character-by-character using buttons or keyboard input.

2.  **Sanitization & Conversion:**
    The `_sanitize_and_prepare()` method translates user symbols (`√`, `^`, `log`) into safe Python equivalents like `math.sqrt`, `**`, and `math.log10`.

3.  **Secure Evaluation:**
    The expression is evaluated using a restricted environment with only `math` functions accessible --> protecting from unsafe code execution.

4.  **Output Display:**
    Results are displayed instantly and added to history (up to 10 latest entries).

---

## 🪄 Future Improvements

-   Add **exponential and factorial** functions
-   Include **graph plotting** (using Matplotlib)
-   Implement **angle mode toggle** (degrees ↔ radians)
-   Save full history to file

---

## 🧑‍💻 Author

> **Developer:**  **Sakshi Chavan**

> **Github:** **[sagesakshi27](https://github.com/sagesakshi27)**

---
