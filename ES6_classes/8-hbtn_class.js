// 8-hbtn_class.js

export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;       // size classe
    this._location = location; // emplacement classe
  }
  
    //numero
  valueOf() {
    return this._size;
  }
    //string
  toString() {
    return this._location;
  }
}
  

  