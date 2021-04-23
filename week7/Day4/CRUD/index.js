const express = require("express");
const app = express();
const cors = require("cors");
const port = process.env.PORT || 3002;
const pool = require("./db.js");


app.use(express.json());
app.use(cors());

app.get("/", (req, res) => {
  res.send("Animal List");
});



app.post("/animal", async (req, res) => {
  try {
    const { name } = req.body;
    
    const newAnimal = await pool.query(
      "INSERT INTO animal (name) VALUES($1)",
      [name]
    );

    res.json(newAnimal);
  } catch (err) {
    console.error(err.message);
  }
});


app.get("/read_animalList", async (req, res) => {
    try {
      const readAnimalList = await pool.query(
        "SELECT * from todo ORDER BY animal_id"
      );
      res.json(readAnimalList.rows);
    } catch (err) {
      console.error(err.message);
    }
  });

  app.put("/update_animal/:id", async (req, res) => {
    try {
      const { id } = req.params;
      const { name } = req.body;
  
      const updateAnimal = await pool.query(
        "UPDATE animal SET description = $1 WHERE animal_id = $2",
        [name, id]
      );
  
      res.json("Updated animal");
    } catch (err) {
      console.error(err.message);
    }
  });

  app.delete("/delete_animal/:id", async (req, res) => {
    try {
      const { id } = req.params;
      const deleteTodoInDB = await pool.query(
        "DELETE FROM animal WHERE animal_id = $1",
        [id]
      );
      res.json("Todo was successfully deleted!");
    } catch (err) {
      console.log(err.message);
    }
  });
  


app.listen(port, () => {
  console.log(`listening on port ${port}`);
});