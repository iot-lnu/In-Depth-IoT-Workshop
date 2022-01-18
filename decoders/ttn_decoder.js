function decodeUplink(input) {
  var payload = input.bytes
  return {
    data: {
      temperature: (payload[0] << 24 >> 16 | payload[1]),
      humidity: payload[2]
    },
    warnings: [],
    errors: []
  };
}
