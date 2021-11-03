function cookingNumbers(num, task1, task2, task3, task4, task5) {
    let myList = [task1, task2, task3, task4, task5]
    let initialNum = parseInt(num)
    for (const task of myList) {
        switch (task) {
            case 'chop' :
                initialNum *= 0.5;
                break
            case 'dice' :
                initialNum = Math.sqrt(initialNum);
                break
            case 'spice' :
                initialNum++;
                break
            case 'bake' :
                initialNum *= 3;
                break
            case 'fillet' :
                initialNum *= 0.8;
                break
        }
        console.log(initialNum)
    }
}