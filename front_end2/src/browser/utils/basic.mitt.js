import mitt from 'mitt';

const emitter = mitt();

// Publish some data on a named topic
function publish(topic, args) {
  emitter.emit(topic, args);
}

// Register a callback on a named topic
function subscribe(topic, callback) {
  emitter.on(topic, callback);
  return [topic, callback];
}

// Disconnect a subscribed function for a topic
function unsubscribe(handle) {
  emitter.off(handle[0], handle[1]);
}

// Publish some data on a named topic, without logging
function publish_no_logging(topic, args) {
  emitter.emit(topic, args);
}

export { publish, subscribe, unsubscribe, publish_no_logging };