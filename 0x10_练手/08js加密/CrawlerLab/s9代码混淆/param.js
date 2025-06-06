! function () {
    "use strict";

    function t(t) {
        t ? (f[0] = f[16] = f[1] = f[2] = f[3] = f[4] = f[5] = f[6] = f[7] = f[8] = f[9] = f[10] = f[11] = f[12] = f[13] =
            f[14] = f[15] = 0, this.blocks = f) : this.blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            this.h0 = 1732584193, this.h1 = 4023233417, this.h2 = 2562383102, this.h3 = 271733878, this.h4 = 3285377520,
            this.block = this.start = this.bytes = this.hBytes = 0, this.finalized = this.hashed = !1, this.first = !0
    }
    var h = "object" == typeof window ? window : {},
        s = !h.JS_SHA1_NO_NODE_JS && "object" == typeof process && process.versions && process.versions.node;
    s && (h = global);
    var i = !h.JS_SHA1_NO_COMMON_JS && "object" == typeof module && module.exports,
        e = "function" == typeof define && define.amd,
        r = "0123456789abcdef".split(""),
        o = [-2147483648, 8388608, 32768, 128],
        n = [24, 16, 8, 0],
        a = ["hex", "array", "digest", "arrayBuffer"],
        f = [],
        u = function (h) {
            return function (s) {
                return new t(!0).update(s)[h]()
            }
        },
        c = function () {
            var h = u("hex");
            s && (h = p(h)), h.create = function () {
                return new t
            }, h.update = function (t) {
                return h.create().update(t)
            };
            for (var i = 0; i < a.length; ++i) {
                var e = a[i];
                h[e] = u(e)
            }
            return h
        },
        p = function (t) {
            var h = eval("require('crypto')"),
                s = eval("require('buffer').Buffer"),
                i = function (i) {
                    if ("string" == typeof i) return h.createHash("sha1").update(i, "utf8").digest("hex");
                    if (i.constructor === ArrayBuffer) i = new Uint8Array(i);
                    else if (void 0 === i.length) return t(i);
                    return h.createHash("sha1").update(new s(i)).digest("hex")
                };
            return i
        };
    t.prototype.update = function (t) {
        if (!this.finalized) {
            var s = "string" != typeof t;
            s && t.constructor === h.ArrayBuffer && (t = new Uint8Array(t));
            for (var i, e, r = 0, o = t.length || 0, a = this.blocks; r < o;) {
                if (this.hashed && (this.hashed = !1, a[0] = this.block, a[16] = a[1] = a[2] = a[3] = a[4] = a[5] =
                    a[6] = a[7] = a[8] = a[9] = a[10] = a[11] = a[12] = a[13] = a[14] = a[15] = 0), s)
                    for (e = this.start; r < o && e < 64; ++r) a[e >> 2] |= t[r] << n[3 & e++];
                else
                    for (e = this.start; r < o && e < 64; ++r)(i = t.charCodeAt(r)) < 128 ? a[e >> 2] |= i << n[3 &
                    e++] : i < 2048 ? (a[e >> 2] |= (192 | i >> 6) << n[3 & e++], a[e >> 2] |= (128 | 63 &
                        i) << n[3 & e++]) : i < 55296 || i >= 57344 ? (a[e >> 2] |= (224 | i >> 12) << n[3 & e++],
                            a[e >> 2] |= (128 | i >> 6 & 63) << n[3 & e++], a[e >> 2] |= (128 | 63 & i) << n[3 & e++]
                    ) : (i = 65536 + ((1023 & i) << 10 | 1023 & t.charCodeAt(++r)), a[e >> 2] |= (240 | i >> 18) <<
                        n[3 & e++], a[e >> 2] |= (128 | i >> 12 & 63) << n[3 & e++], a[e >> 2] |= (128 | i >> 6 &
                        63) << n[3 & e++], a[e >> 2] |= (128 | 63 & i) << n[3 & e++]);
                this.lastByteIndex = e, this.bytes += e - this.start, e >= 64 ? (this.block = a[16], this.start = e -
                    64, this.hash(), this.hashed = !0) : this.start = e
            }
            return this.bytes > 4294967295 && (this.hBytes += this.bytes / 4294967296 << 0, this.bytes = this.bytes %
                4294967296), this
        }
    }, t.prototype.finalize = function () {
        if (!this.finalized) {
            this.finalized = !0;
            var t = this.blocks,
                h = this.lastByteIndex;
            t[16] = this.block, t[h >> 2] |= o[3 & h], this.block = t[16], h >= 56 && (this.hashed || this.hash(),
                t[0] = this.block, t[16] = t[1] = t[2] = t[3] = t[4] = t[5] = t[6] = t[7] = t[8] = t[9] = t[10] =
                t[11] = t[12] = t[13] = t[14] = t[15] = 0), t[14] = this.hBytes << 3 | this.bytes >>> 29, t[15] =
                this.bytes << 3, this.hash()
        }
    }, t.prototype.hash = function () {
        var t, h, s = this.h0,
            i = this.h1,
            e = this.h2,
            r = this.h3,
            o = this.h4,
            n = this.blocks;
        for (t = 16; t < 80; ++t) h = n[t - 3] ^ n[t - 8] ^ n[t - 14] ^ n[t - 16], n[t] = h << 1 | h >>> 31;
        for (t = 0; t < 20; t += 5) s = (h = (i = (h = (e = (h = (r = (h = (o = (h = s << 5 | s >>> 27) + (i & e |
            ~i & r) + o + 1518500249 + n[t] << 0) << 5 | o >>> 27) + (s & (i = i << 30 |
            i >>> 2) | ~s & e) + r + 1518500249 + n[t + 1] << 0) << 5 | r >>> 27) + (o & (s = s <<
            30 | s >>> 2) | ~o & i) + e + 1518500249 + n[t + 2] << 0) << 5 | e >>> 27) + (r & (o = o <<
            30 | o >>> 2) | ~r & s) + i + 1518500249 + n[t + 3] << 0) << 5 | i >>> 27) + (e & (r = r << 30 | r >>>
            2) | ~e & o) + s + 1518500249 + n[t + 4] << 0, e = e << 30 | e >>> 2;
        for (; t < 40; t += 5) s = (h = (i = (h = (e = (h = (r = (h = (o = (h = s << 5 | s >>> 27) + (i ^ e ^ r) +
            o + 1859775393 + n[t] << 0) << 5 | o >>> 27) + (s ^ (i = i << 30 | i >>> 2) ^
            e) + r + 1859775393 + n[t + 1] << 0) << 5 | r >>> 27) + (o ^ (s = s << 30 | s >>>
            2) ^ i) + e + 1859775393 + n[t + 2] << 0) << 5 | e >>> 27) + (r ^ (o = o << 30 | o >>> 2) ^
            s) + i + 1859775393 + n[t + 3] << 0) << 5 | i >>> 27) + (e ^ (r = r << 30 | r >>> 2) ^ o) + s +
            1859775393 + n[t + 4] << 0, e = e << 30 | e >>> 2;
        for (; t < 60; t += 5) s = (h = (i = (h = (e = (h = (r = (h = (o = (h = s << 5 | s >>> 27) + (i & e | i & r |
            e & r) + o - 1894007588 + n[t] << 0) << 5 | o >>> 27) + (s & (i = i << 30 |
            i >>> 2) | s & e | i & e) + r - 1894007588 + n[t + 1] << 0) << 5 | r >>> 27) + (o &
            (s = s << 30 | s >>> 2) | o & i | s & i) + e - 1894007588 + n[t + 2] << 0) << 5 | e >>>
            27) + (r & (o = o << 30 | o >>> 2) | r & s | o & s) + i - 1894007588 + n[t + 3] << 0) << 5 | i >>>
            27) + (e & (r = r << 30 | r >>> 2) | e & o | r & o) + s - 1894007588 + n[t + 4] << 0, e = e << 30 |
            e >>> 2;
        for (; t < 80; t += 5) s = (h = (i = (h = (e = (h = (r = (h = (o = (h = s << 5 | s >>> 27) + (i ^ e ^ r) +
            o - 899497514 + n[t] << 0) << 5 | o >>> 27) + (s ^ (i = i << 30 | i >>> 2) ^
            e) + r - 899497514 + n[t + 1] << 0) << 5 | r >>> 27) + (o ^ (s = s << 30 | s >>> 2) ^
            i) + e - 899497514 + n[t + 2] << 0) << 5 | e >>> 27) + (r ^ (o = o << 30 | o >>> 2) ^ s) +
            i - 899497514 + n[t + 3] << 0) << 5 | i >>> 27) + (e ^ (r = r << 30 | r >>> 2) ^ o) + s - 899497514 +
            n[t + 4] << 0, e = e << 30 | e >>> 2;
        this.h0 = this.h0 + s << 0, this.h1 = this.h1 + i << 0, this.h2 = this.h2 + e << 0, this.h3 = this.h3 + r <<
            0, this.h4 = this.h4 + o << 0
    }, t.prototype.hex = function () {
        this.finalize();
        var t = this.h0,
            h = this.h1,
            s = this.h2,
            i = this.h3,
            e = this.h4;
        return r[t >> 28 & 15] + r[t >> 24 & 15] + r[t >> 20 & 15] + r[t >> 16 & 15] + r[t >> 12 & 15] + r[t >> 8 &
        15] + r[t >> 4 & 15] + r[15 & t] + r[h >> 28 & 15] + r[h >> 24 & 15] + r[h >> 20 & 15] + r[h >> 16 &
        15] + r[h >> 12 & 15] + r[h >> 8 & 15] + r[h >> 4 & 15] + r[15 & h] + r[s >> 28 & 15] + r[s >> 24 &
        15] + r[s >> 20 & 15] + r[s >> 16 & 15] + r[s >> 12 & 15] + r[s >> 8 & 15] + r[s >> 4 & 15] + r[15 &
        s] + r[i >> 28 & 15] + r[i >> 24 & 15] + r[i >> 20 & 15] + r[i >> 16 & 15] + r[i >> 12 & 15] + r[i >>
        8 & 15] + r[i >> 4 & 15] + r[15 & i] + r[e >> 28 & 15] + r[e >> 24 & 15] + r[e >> 20 & 15] + r[e >>
        16 & 15] + r[e >> 12 & 15] + r[e >> 8 & 15] + r[e >> 4 & 15] + r[15 & e]
    }, t.prototype.toString = t.prototype.hex, t.prototype.digest = function () {
        this.finalize();
        var t = this.h0,
            h = this.h1,
            s = this.h2,
            i = this.h3,
            e = this.h4;
        return [t >> 24 & 255, t >> 16 & 255, t >> 8 & 255, 255 & t, h >> 24 & 255, h >> 16 & 255, h >> 8 & 255,
            255 & h, s >> 24 & 255, s >> 16 & 255, s >> 8 & 255, 255 & s, i >> 24 & 255, i >> 16 & 255, i >> 8 &
            255, 255 & i, e >> 24 & 255, e >> 16 & 255, e >> 8 & 255, 255 & e]
    }, t.prototype.array = t.prototype.digest, t.prototype.arrayBuffer = function () {
        this.finalize();
        var t = new ArrayBuffer(20),
            h = new DataView(t);
        return h.setUint32(0, this.h0), h.setUint32(4, this.h1), h.setUint32(8, this.h2), h.setUint32(12, this.h3),
            h.setUint32(16, this.h4), t
    };
    var y = c();
    i ? global.md5 = y : (h.md5 = y, e && define(function () {
        return y
    }))
}();
function Base64() {
        // private property
        _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
        // public method for encoding
        this.encode = function (input) {
            var output = "";
            var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
            var i = 0;
            input = _utf8_encode(input);
            while (i < input.length) {
                chr1 = input.charCodeAt(i++);
                chr2 = input.charCodeAt(i++);
                chr3 = input.charCodeAt(i++);
                enc1 = chr1 >> 2;
                enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
                enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
                enc4 = chr3 & 63;
                if (isNaN(chr2)) {
                    enc3 = enc4 = 64;
                } else if (isNaN(chr3)) {
                    enc4 = 64;
                }
                output = output +
                    _keyStr.charAt(enc1) + _keyStr.charAt(enc2) +
                    _keyStr.charAt(enc3) + _keyStr.charAt(enc4);
            }
            return output;
        };

        // public method for decoding
        this.decode = function (input) {
            var output = "";
            var chr1, chr2, chr3;
            var enc1, enc2, enc3, enc4;
            var i = 0;
            input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
            while (i < input.length) {
                enc1 = _keyStr.indexOf(input.charAt(i++));
                enc2 = _keyStr.indexOf(input.charAt(i++));
                enc3 = _keyStr.indexOf(input.charAt(i++));
                enc4 = _keyStr.indexOf(input.charAt(i++));
                chr1 = (enc1 << 2) | (enc2 >> 4);
                chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
                chr3 = ((enc3 & 3) << 6) | enc4;
                output = output + String.fromCharCode(chr1);
                if (enc3 != 64) {
                    output = output + String.fromCharCode(chr2);
                }
                if (enc4 != 64) {
                    output = output + String.fromCharCode(chr3);
                }
            }
            output = _utf8_decode(output);
            return output;
        };

        // private method for UTF-8 encoding
        _utf8_encode = function (string) {
            string = string.replace(/\r\n/g,"\n");
            var utftext = "";
            for (var n = 0; n < string.length; n++) {
                var c = string.charCodeAt(n);
                if (c < 128) {
                    utftext += String.fromCharCode(c);
                } else if((c > 127) && (c < 2048)) {
                    utftext += String.fromCharCode((c >> 6) | 192);
                    utftext += String.fromCharCode((c & 63) | 128);
                } else {
                    utftext += String.fromCharCode((c >> 12) | 224);
                    utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                    utftext += String.fromCharCode((c & 63) | 128);
                }

            }
            return utftext;
        };

        // private method for UTF-8 decoding
        _utf8_decode = function (utftext) {
            var string = "";
            var i = 0;
            var c = c1 = c2 = 0;
            while ( i < utftext.length ) {
                c = utftext.charCodeAt(i);
                if (c < 128) {
                    string += String.fromCharCode(c);
                    i++;
                } else if((c > 191) && (c < 224)) {
                    c2 = utftext.charCodeAt(i+1);
                    string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                    i += 2;
                } else {
                    c2 = utftext.charCodeAt(i+1);
                    c3 = utftext.charCodeAt(i+2);
                    string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                    i += 3;
                }
            }
            return string;
        };
    };
function uuid() {
        var s = [];
        var hexDigits = "0123456789abcdefghijklmnopqrstuvwxyz";
        for (var i = 0; i < 36; i++) {
            s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
        }
        s[14] = "4";
        s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);
        s[8] = s[13] = s[18] = s[23] = "-";
        var uuid = s.join("");
        return uuid;
}
const getparam = function () {
    // "use strict";
    let base64 = new Base64();
    let key = uuid();
    let time= (Math.floor(( new Date().getTime() + 10010) / 99)).toString();
    let sign = md5(key + base64.encode(time));
    let param = {
        "key": key,
        "time": time,
        "sign": sign
    };
    return param
};
// render(getparam());


module.exports={
    getparam
};
