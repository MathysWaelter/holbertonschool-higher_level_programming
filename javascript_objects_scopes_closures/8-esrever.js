#!/usr/bin/node
exports.esrever = function (list) {
  const scd = [];
  while (list.length) {
    scd.push(list.pop());
  }
  return scd;
};
