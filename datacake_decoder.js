// Paste this snippet under device/configuration/Payload Decoder

function Decoder(payload, port) {
    if(port === 1 || port === 2) {
        return [
          {
              field: "TEMPERATURE",
              // value: payload[0] // Unsigned and only one byte
              // To view negative values, we shift bits.
              value: (payload[0] << 24 >> 16 | payload[1]) // / 100
          },
          {
              field: "HUMIDITY",
              value: payload[2]
          }
        ];
    }
}
