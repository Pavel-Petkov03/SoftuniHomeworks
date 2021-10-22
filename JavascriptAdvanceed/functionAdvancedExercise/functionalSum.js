function add(result) {

    function main(num) {
        result += num
        return main
    }

    main.toString = () => result

    return main
}