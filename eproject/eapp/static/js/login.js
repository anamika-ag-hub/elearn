const toggleBtn = document.getElementById("toggleForm");
const formTitle = document.getElementById("formTitle");
const authForm = document.getElementById("authForm");
const submitBtn = document.getElementById("submitBtn");
const successMsg = document.getElementById("successMessage");
const emailGroup = document.querySelector(".email-group");
const confirmGroup = document.querySelector(".confirm-group");
const themeToggle = document.getElementById("themeToggle");

let isLogin = true;

toggleBtn.addEventListener("click", (e) => {
  e.preventDefault();
  isLogin = !isLogin;

  // Update UI
  formTitle.textContent = isLogin ? "Login" : "Sign Up";
  submitBtn.textContent = isLogin ? "Login" : "Sign Up";
  toggleBtn.textContent = isLogin ? "Sign up" : "Login";

  toggleBtn.previousSibling.textContent = isLogin
    ? "Don’t have an account? "
    : "Already have an account? ";

  // Toggle extra fields
  emailGroup.classList.toggle("hidden", isLogin);
  confirmGroup.classList.toggle("hidden", isLogin);

  // Smooth transition
  authForm.style.opacity = 0;
  setTimeout(() => {
    authForm.style.opacity = 1;
  }, 300);
});

authForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const pass = document.getElementById("password").value;
  const confirm = document.getElementById("confirmPassword").value;

  if (!isLogin && pass !== confirm) {
    alert("Passwords do not match!");
    return;
  }

  // Simulate success
  authForm.style.transition = "all 0.4s ease";
  authForm.style.transform = "scaleY(0)";
  authForm.style.opacity = 0;

  setTimeout(() => {
    authForm.style.display = "none";
    successMsg.style.display = "block";
  }, 400);
});

// Theme toggle
themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("pink");
});
