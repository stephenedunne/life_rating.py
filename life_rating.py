def mental_health_rating():
    mental_health_number = input("On a scale of 1-10, how would you currently rate your mental health?\n")
    mental_health_explanation = input("In 255 characters, explain why you said \"" + mental_health_number + "\":\n")

def physical_health_rating():
    physical_health_number = input("On a scale of 1-10, how would you currently rate your physical health?\n")
    physcial_health_explanation = input("In 255 characters, explain why you said \"" + physical_health_number + "\":\n")

def financial_health_rating():
    financial_health_number = input("On a scale of 1-10, how would you currently rate your financial health?\n")
    financial_health_explanation = input("In 255 characters, explain why you said \"" + financial_health_number + "\":\n")

def work_life_rating():
    work_life_number = input("On a scale of 1-10, how would you currently rate your work life?\n")
    work_life_explanation = input("In 255 characters, explain why you said \"" + work_life_number + "\":\n")

def main():
    mental_health_rating()
    physical_health_rating()
    work_life_rating()

if __name__ == "__main__":
    main()
