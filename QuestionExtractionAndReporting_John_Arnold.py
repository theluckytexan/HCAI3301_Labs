

inpuTFeedback = "customer_feedback.txt"
reporTFeedback = "questions_report_John_Arnold.txt"


def main():
    questionNumber = 0
    totaLFeedbacks = 0

    f = open(inpuTFeedback, "r")

    lines = []
    lines.append("**************************************")
    lines.append("** Report of Questions by Customers **")
    lines.append("**************************************")

    for blanKLine in f:
        line = blanKLine.strip()
        if not line:
            continue

        totaLFeedbacks += 1

        if "||" in line:
            parts = line.split("||", 1)
            name = parts[0].strip()
            feedback = parts[1].strip() if len(parts) > 1 else ""
        else:
            name = "Unknown"
            feedback = line

        for sentence in feedback.split("."):
            sentence = sentence.strip()
            if sentence == "":
                continue

            questioNParts = sentence.split("?")
            for i in range(len(questioNParts) - 1):
                questioNText = questioNParts[i].strip()
                if questioNText:
                    questionNumber += 1
                    lines.append(f"{questionNumber}) {name} asked: {questioNText}?")


    f.close()

    lines.append("------------------------------------------------------")
    lines.append(f"No. of Feedbacks Processed: {totaLFeedbacks}")
    lines.append(f"No. of Extracted Questions: {questionNumber}")
    lines.append("*************************************")

    out = open(reporTFeedback, "w")
    out.write("\n".join(lines))
    out.close()

    print(f"Report created: '{reporTFeedback}'")
    print(f"Feedback processed: {totaLFeedbacks} | Questions extracted: {questionNumber}")


if __name__ == "__main__":
    main()
