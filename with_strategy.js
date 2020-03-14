const PRICING_STRATEGIES = {
    'gold': (price) => (price - 30),
    'silver': (price) => (price - 20),
    'normal': (price) => (price - 10)
};

class User {
    setMembership(membership) {
        this.membership = membership;
    }

    getDiscountedPrice(price) {
        return PRICING_STRATEGIES[this.membership].call(null, price)
    }
}

// our user code becomes much cleaner.
user = new User();
user.price = 40;
user.setMembership('gold');
console.log(user.getDiscountedPrice(user.price));
// we can dynamically change membership
user.setMembership('normal');
console.log(user.getDiscountedPrice(user.price));