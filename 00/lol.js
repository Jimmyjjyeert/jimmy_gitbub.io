function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    // 這裡可以替換成檢查資料庫或其他驗證方式
    if (username === "admin" && password === newFunction()) {
      alert("Login successful!");
    } else {
      alert("Incorrect username or password.");
    }

    function newFunction() {
        return "password";
    }
  }
  