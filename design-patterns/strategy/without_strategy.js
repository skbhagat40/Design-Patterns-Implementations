class User {
    constructor(membership) {
        this.membership = membership
    }

    getDiscountedPrice(price) {
        if (this.membership === 'gold')
            return price - 30;
        else if (this.membership === 'silver')
            return price - 20;
        else if (this.membership === 'normal')
            return price
    }
}

user = new User('gold');
console.log(user.getDiscountedPrice(40));