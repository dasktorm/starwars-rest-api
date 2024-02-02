const login = async (userInput) => {
  const { username, password } = userInput;

  try {
    const response = await fetch(
      `${import.meta.env.VITE_API_URL}api/auth/login`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      }
    );

    const data = await response.json();
    localStorage.setItem("jwt-token", data.token);
    console.log(data.token);
    return data;
  } catch (error) {
    console.log(error);
  }
};

export default login;
