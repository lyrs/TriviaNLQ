import * as React from "react";
import { useState, useEffect } from "react";
import colorLogo from "./asset/ColorLogo.png";
import "./App.css";
import {
  FormControl,
  Input,
  InputLabel,
  IconButton,
  InputAdornment,
  CircularProgress,
} from "@mui/material";
import { Search as SearchIcon } from "@mui/icons-material";
import { useLocation } from "react-router-dom";
import Result from "./result";

const SearchPage = (props) => {
  const { state } = useLocation();
  const [searchText, setSearchText] = useState(state.searchText);
  const [loading, setLoading] = useState(true);
  const [result, setResult] = useState(null);

  const callApi = async () => {
    setLoading(true);
    console.log("calling API for Query: " + searchText);
    const requestOptions = {
      method: "POST",
      mode: "cors",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ searchText: searchText }),
    };
    try {
      var response = await fetch("http://127.0.0.1:5000", requestOptions);
    } catch (error) {
      console.log("There was an error", error);
    }
    if (response?.ok) {
      setResult(await response.json());
    } else {
      console.log(`HTTP Response Code: ${response?.status}`);
    }
    setLoading(false);
  };

  useEffect(() => {
    //api Call
    callApi();
  }, []);

  return (
    <div
      style={{
        width: "100%",
        height: "100vh",
      }}
    >
      <div
        style={{
          display: "flex",
          widht: "100%",
          height: "20vh",
          background: "#fa9632",
          flexDirection: "row",
        }}
      >
        <img
          src={colorLogo}
          style={{
            display: "flex",
            height: "15vh",
            marginTop: "auto",
            marginBottom: "auto",
            paddingLeft: 5,
          }}
        />
        <div
          style={{
            width: "500%",
            display: "flex",
            justifyContent: "flex-start",
            marginTop: "auto",
            marginLeft: "5%",
            marginBottom: "auto",
          }}
        >
          <FormControl sx={{ width: "85%" }} variant="standard">
            <InputLabel
              htmlFor="search"
              style={{ color: "black", fontSize: 20 }}
            >
              Ask your Knowledge Base
            </InputLabel>
            <Input
              id="search"
              type={"text"}
              variant="standard"
              sx={{ input: { fontSize: 40, color: "white" } }}
              value={searchText}
              onChange={(event) => {
                setSearchText(event.target.value);
              }}
              onKeyPress={(e) => {
                if (e.key === "Enter" && !loading) callApi();
              }}
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="search"
                    onClick={() => {
                      if (!loading) callApi();
                    }}
                    edge="end"
                  >
                    <SearchIcon style={{ color: "white", fontSize: "60px" }} />
                  </IconButton>
                </InputAdornment>
              }
            />
          </FormControl>
        </div>
      </div>
      <div style={{ display: "flex", width: "100%", height: "80vh" }}>
        <div
          style={{
            width: "100%",
            marginLeft: "auto",
            marginRight: "auto",
            display: "flex",
            flexDirection: "row",
            justifyContent: "center",
          }}
        >
          {loading || result == null ? (
            <CircularProgress
              size="250px"
              sx={{ marginTop: "80px", color: "#fa9632" }}
            />
          ) : (
            <Result result={result} />
          )}
        </div>
      </div>
    </div>
  );
};

export default SearchPage;
