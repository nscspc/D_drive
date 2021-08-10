import React from "react";
function Footer() {
  var curryear = new Date().getFullYear();
  //Date() is a inbuilt function to get the date and current time as well.
  // so we are using a function getFullYear() to get only year.
  return (
    <footer>
      <p>Copyright @ {curryear}</p>
    </footer>
  );
}

export default Footer;
