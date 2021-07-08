# 1254732 Mauricio Corado
least = 18
most = 75


def get_age():                      # get age method uses to error check the age parameters
    age = int(input())

    if (least > age) or (age > most):
        raise ValueError('Invalid age.')
    return age


def fat_burning_heart_rate(age):          # method used to calculate the equation needed
    hr = ((220 - age) * .7)
    return hr

if __name__ == "__main__":      # main code checks for value error
    try:
        age = get_age()
        hr = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age, hr))
    except ValueError as wrong:
        print(wrong)
        print('Could not calculate heart rate info.')