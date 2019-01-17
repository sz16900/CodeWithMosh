// In node, every file is a module
const EventEmitter = require('events');

const Logger = require('./logger');
const logger = new Logger();

// Register a listener 
logger.on('messageLogged', (arg) => {
    console.log('lister called', arg);
});

logger.log('message');