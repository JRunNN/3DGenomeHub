let _noop = function() {};
/**
 * 队列
 */
class Queue extends Set {
    constructor(iterable) {
        super(iterable);
    }

    /**
     * 添加一个元素到队列尾部
     */
    push(el) {
        this.add(el);
    }

/**
 * 移除并返回队列头部的元素
 */
    put() {
        let el;
        for (el of this) { break; }
        this.delete(el);
        
        return el;
    }
}


 