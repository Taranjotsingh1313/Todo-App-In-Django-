const add = document.getElementById("add");
const add_form = document.getElementById("add_form");
add.onclick = () => {
  if (add_form.style.display == "none") add_form.style.display = "flex";
  else {
    add_form.style.display = "none";
  }
};
