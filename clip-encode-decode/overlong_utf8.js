function toOverlongUTF8(hex) {
  const codePoint = parseInt(hex, 16);
  let m = (b) => '%' + b.toString(16).toUpperCase();
  if (codePoint < 0x80) {
    let two_byte = [0xC0 | (codePoint >> 6), 0x80 | (codePoint & 0x3F)]
    let three_byte = [0xE0,0x80,0x80 | (codePoint & 0x3F)]
    return two_byte.map(m).join('')+' / '+three_byte.map(m).join('');
  } else {
    throw new Error("Only works for ASCII characters");
  }
}

console.log(toOverlongUTF8("3e"));
