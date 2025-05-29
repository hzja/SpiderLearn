window = global;
const JSEncrypt = require('jsencrypt'); //暂时不知道为啥要导入这个库
const CryptoJS = require('crypto-js'); //暂时不知道为啥要导入这个库

function EncryptParams(t) {
    t = t || {};
    var e = function(t) {
      for (var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", i = "", r = 0; r < t; r++) {
        var n = Math.floor(Math.random() * e.length);
        i += e.substring(n, n + 1)
      }
      return i
    }(16)
      , i = new JSEncrypt({}); //不知道为啥要用JSEncrypt
    i.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYEVrK/4Mahiv0pUJgTybx4J9P5dUT/Y0PuwMbk+gMU+jrZnBiXGv6/hCH1avIhoBcE535F8nJQQN3UavZdFkYidsoXuEnat3+eVTp3FslyhRwIBDF09v4vDhRtxFOT+R7uH7h/mzmyA2/+lfIMWGIrffXprYizbV76+YQKhoqFQIDAQAB");
    var r = i.encrypt(window.btoa(e))
      , s = CryptoJS.enc.Utf8.parse("0102030405060708") //不知道为啥要用CryptoJS.enc.Utf8
      , h = CryptoJS.enc.Utf8.parse(e) //不知道为啥要用CryptoJS.enc.Utf8
      , u = window.btoa(Object.keys(t).join(","))
      , c = {};
    return Object.keys(t).forEach((function(e) {
      var i = t[e]
        , r = CryptoJS.AES.encrypt(i, h, {
        iv: s,
        padding: CryptoJS.pad.Pkcs7 //这里的padding暂时不知道为啥要这样写
      });
      r = r.toString(),
      c[e] = r
    }
    )),
    {
      EUI: "".concat(r, ".").concat(u),
      encryptedParams: c
    }
  }
  
  const user = "18814317942"
  const EncryptParam = EncryptParams({
      "user":user 
    })
 console.log(EncryptParam)
 console.log("EUI:" + EncryptParam.EUI)
 console.log("EncryptedParams:" + EncryptParam.encryptedParams["user"])