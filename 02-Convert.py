num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
def spell(num):
    if num == 0:
        return ""
    if num < 20:
        return (num2words[num])
    elif num < 100:
        ray = divmod(num,10)
        return (num2words2[ray[0]-2]+" "+spell(ray[1]))
    elif num <1000:
        ray = divmod(num,100)
        if ray[1] == 0:
            mid = " hundred"
        else:
            mid =" hundred and "
        return(num2words[ray[0]]+mid+spell(ray[1]))
print(spell(1))
print(spell(12))
print(spell(30))