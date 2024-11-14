#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);

  const characters = data.characters;

  const printCharacter = (index) => {
    if (index >= characters.length) return;

    request(characters[index], (error, response, body) => {
      if (!error) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        printCharacter(index + 1);
      }
    });
  };

  printCharacter(0);
});
