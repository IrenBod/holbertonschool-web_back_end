// 7-airport.js

class Airport {
    constructor(name, code) {
      this._name = name;
      this._code = code;
    }
  
    // Override the default toString method
    toString() {
      return `[object ${this._code}]`;
    }
  }
  
  export default Airport;
  