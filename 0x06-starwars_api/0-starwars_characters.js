#!/usr/bin/node

/**
 * Star wars api
 * Script that prints all characters of a Star Wars movie:
 */
const request = require('request');
const filmId = process.argv[2];
if (!filmId || isNaN(filmId)) {
  process.exit(1);
}
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const respPromises = [];

  const json = JSON.parse(body);
  const characters = json.characters;

  characters.forEach((character) => {
    const url = character;
    const promise = new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        const json = JSON.parse(body);
        resolve(json.name);
      });
    });
    respPromises.push(promise);
  });
  Promise.all(respPromises).then((values) => {
    values.forEach((value) => {
      console.log(value);
    });
  }).catch((error) => {
    console.log(error);
  });
});
