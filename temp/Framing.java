import java.util.Scanner;

public class Framing {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the Data Stream: ");
        String dataStream = scanner.nextLine();

        System.out.println("1. Character Count");
        System.out.println("2. Byte Stuffing");
        System.out.println("3. Bit Stuffing");
        System.out.println("4. Physical Data Violation");

        System.out.print("Enter the number for the corresponding Framing technique: ");
        int choice = scanner.nextInt();

        String result = "";
        switch (choice) {
            case 1:
                result = characterCount(dataStream);
                break;
            case 2:
                result = byteStuffing(dataStream);
                break;
            case 3:
                result = bitStuffing(dataStream);
                break;
            case 4:
                result = physicalDataViolation(dataStream);
                break;
            default:
                System.out.println("Invalid choice!");
                System.exit(0);
        }

        System.out.println("The Frame after Processing is: " + result);
    }

    public static String characterCount(String dataStream) {
        StringBuilder result = new StringBuilder();
        int maxFrameSize = 9;
        int currentIndex = 0;

        while (currentIndex < dataStream.length()) {
            // Calculate the maximum size for data part considering 1 digit for length
            int availableSize = maxFrameSize - 1;  // 1 for the character count digit
            int endIndex = Math.min(currentIndex + availableSize, dataStream.length());
            String dataPart = dataStream.substring(currentIndex, endIndex);
            String lengthPrefix = String.valueOf(dataPart.length());

            // Construct frame
            String frame = lengthPrefix + dataPart;
            result.append(frame);
            currentIndex = endIndex;
        }

        return result.toString();
    }

    public static String byteStuffing(String dataStream) {
        // Assuming 'ESC' character as 'E' and flag character as 'F' for simplicity
        String stuffedStream = "";
        for (int i = 0; i < dataStream.length(); i++) {
            char ch = dataStream.charAt(i);
            if (ch == 'F' || ch == 'E') {
                stuffedStream += "E";  // Insert ESC before F or E
            }
            stuffedStream += ch;
        }
        return "F" + stuffedStream + "F";  // Adding flag characters at the start and end
    }

    public static String bitStuffing(String dataStream) {
        String stuffedStream = "";
        int consecutiveOnes = 0;

        for (int i = 0; i < dataStream.length(); i++) {
            char ch = dataStream.charAt(i);
            if (ch == '1') {
                consecutiveOnes++;
                stuffedStream += '1';
                if (consecutiveOnes == 5) {
                    stuffedStream += '0';  // Insert '0' after five consecutive '1's
                    consecutiveOnes = 0;
                }
            } else {
                stuffedStream += '0';
                consecutiveOnes = 0;
            }
        }
        return stuffedStream;
    }

    public static String physicalDataViolation(String dataStream) {
        // Simple example: Appending a special code "01" to indicate physical violation
        return dataStream + "01";
    }
}
