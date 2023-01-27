import * as React from "react";

const Result = (props) => {
  var result = props.result;

  const queryData = (label, data) => {
    return (
      <div
        style={{
          width: "95%",
          display: "flex",
          flexDirection: "column",
          padding: "10px",
        }}
      >
        <div style={{ width: "15%", fontSize: "20px" }}>{label + ":"}</div>
        <div
          style={{
            backgroundColor: "rgba(250, 150, 50, 0.6)",
            padding: "10px",
            borderRadius: "10px",
            fontSize: "20px",
          }}
        >
          {data}
        </div>
      </div>
    );
  };

  const dbpediaResultTable = (binding, variables) => {
    return (
      <div
        style={{
          display: "flex",
          flex: 1,
          flexDirection: "row",
        }}
      >
        {variables.map((x) => {
          return (
            <div
              style={{
                display: "flex",
                flex: 1,
                justifyContent: "space-around",
                padding: "2px",
                margin: "2px",
                backgroundColor: "white",
              }}
            >
              {binding[x].value}
            </div>
          );
        })}
      </div>
    );
  };

  const dbpediaResultParser = (dbpediaResult) => {
    if (dbpediaResult.results != null) {
      var variables = dbpediaResult.head.vars;

      return (
        <>
          <div
            style={{
              display: "flex",
              flex: 1,
              flexDirection: "row",
            }}
          >
            {variables
              ? variables.map((_var) => {
                  return (
                    <div
                      style={{
                        display: "flex",
                        flex: 1,
                        justifyContent: "space-around",
                        padding: "2px",
                        margin: "2px",
                        borderRadius: "5px",
                        color: "white",
                        backgroundColor: "rgba(250, 150, 50, 0.5)",
                      }}
                    >
                      {_var}
                    </div>
                  );
                })
              : null}
          </div>
          {dbpediaResult.results.bindings.map((binding, index) => {
            return (
              <div
                key={index}
                style={{ display: "flex", flexDirection: "column", flex: 1 }}
              >
                {dbpediaResultTable(binding, variables)}
              </div>
            );
          })}
        </>
      );
    } else if (dbpediaResult.boolean != null) {
      return dbpediaResult.boolean.toString();
    }
  };

  return (
    <div
      style={{
        width: "100%",
        paddingTop: "30px",
        paddingLeft: "30px",
        fontSize: "35px",
      }}
    >
      <div>
        {result.questionEncoding != null
          ? queryData(
              "Question Inference",
              result.questionEncoding.split("\t")[1]
            )
          : null}
      </div>
      <div>{queryData("Embedded Query", result.queryEncoding)}</div>
      <div>{queryData("Parsed Query", result.sparql)}</div>
      <div>
        {result.error
          ? queryData("Error", result.error)
          : result.dbpediaResult
          ? queryData("Result", dbpediaResultParser(result.dbpediaResult))
          : null}
      </div>
    </div>
  );
};

export default Result;
