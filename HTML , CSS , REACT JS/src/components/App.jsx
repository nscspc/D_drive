import React from "react";
import Header from "./Header"; //as App and Header is present in same folder so no need to write "./components/Header".
import Footer from "./Footer";
import Note from "./Note";

function App() {
  return (
    <div>
      <Header />
      <Note />
      <Note />
      <Note />
      <Note />
      <Footer />
    </div>
  );
}

export default App;
