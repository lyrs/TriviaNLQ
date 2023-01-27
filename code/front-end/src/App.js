import * as React from "react";
import { useState } from "react";
import colorLogo from "./asset/ColorLogo.png";
import "./App.css";
import {
  FormControl,
  Input,
  InputLabel,
  IconButton,
  InputAdornment,
} from "@mui/material";
import { Search as SearchIcon } from "@mui/icons-material";
import { useNavigate } from "react-router-dom";

function App() {
  const [searchText, setSearchText] = useState("");
  const navigate = useNavigate();

  const search = () => {
    navigate("/search", { state: { searchText: searchText } });
  };

  return (
    <div style={{ width: "100%", height: "100vh" }}>
      <div
        style={{
          display: "flex",
          widht: "100%",
          height: "40vh",
          background: "#fa9632",
          flex: 1,
          flexDirection: "column",
        }}
      >
        <img
          src={colorLogo}
          style={{
            height: "30vh",
            margin: "auto",
            display: "flex",
          }}
        />
      </div>
      <div
        style={{
          width: "100%",
          display: "flex",
          justifyContent: "space-around",
          marginTop: "100px",
        }}
      >
        <FormControl sx={{ m: 1, width: "50%" }} variant="standard">
          <InputLabel htmlFor="search" style={{ fontSize: 20 }}>
            Ask your Knowledge Base
          </InputLabel>
          <Input
            id="search"
            type={"text"}
            variant="standard"
            sx={{ input: { fontSize: 40 } }}
            value={searchText}
            onChange={(event) => {
              setSearchText(event.target.value);
            }}
            onKeyPress={(e) => {
              if (e.key === "Enter") search();
            }}
            endAdornment={
              <InputAdornment position="end">
                <IconButton
                  aria-label="search"
                  onClick={() => search()}
                  edge="end"
                >
                  <SearchIcon style={{ color: "#fa9632", fontSize: "60px" }} />
                </IconButton>
              </InputAdornment>
            }
          />
        </FormControl>
      </div>
    </div>
  );
}

export default App;
