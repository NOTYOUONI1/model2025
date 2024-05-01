const express = require('express')
const router = express.Router()
const mongo = require('../mongo')


router.get('/',(req, res)=>{
    res.send(mongo)
})
module.exports= router