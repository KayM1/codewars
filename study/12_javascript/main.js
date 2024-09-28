function main() {
    // Log a message to the console
    console.log("Hello, world! This is a console message.");

    // Perform a simple calculation and log the result
    const a = 5;
    const b = 10;
    const sum = a + b;

    console.log(`The sum of ${a} and ${b} is ${sum}.`);

    // Example of using setTimeout to delay a message
    setTimeout(() => {
        console.log("This message is displayed after a 2 second delay.");
    }, 2000);
}

main();