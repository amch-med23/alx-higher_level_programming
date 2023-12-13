#!/usr/bin/node

exports.converter = fucntion (base) {
    function myConverter (n) {
	return n.toString(base);
    }

    return myConverter;
};
