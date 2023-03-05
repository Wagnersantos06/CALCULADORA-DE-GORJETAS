print('-'*35)
print('CALCULADORA DE GORJETAS')
print('-'*35)

print()

cont = 'S'

while (cont == 'S' or cont == 'Sim'):

    valor_conta = float(input('''Digite o valor da conta:
'''))
    
    gorjeta = float(input('''Digite o percentual de gorjeta que você gostaria de pagar:
'''))
    
    rachar = input('Você gostaria de rachar a conta ? (S / N)').capitalize()
    
    if (rachar == 'S' or rachar == 'Sim'):
        qtd_rachar = int(input('''Você quer rachar em quantas pessoas: 
'''))
        
        v_gorjeta = (gorjeta / 100) * valor_conta
        valor_total = valor_conta + v_gorjeta
        div = valor_total / qtd_rachar
    
        print('O valor da gorjeta será de {:.2f} e com isso o total da conta será de {:.2f}'.format(v_gorjeta,     valor_total))
        print()
        print('Divindo ele em {} ficará {:.2f} a ser pago por pessoa'.format(qtd_rachar, div))
        print()
        print('Muito Obrigado!')

    else:
        
        v_gorjeta = (gorjeta / 100) * valor_conta
        valor_total = valor_conta + v_gorjeta

        print('O valor da gorjeta será de {:.2f} e com isso o total da conta será de {:.2f}'.format(v_gorjeta, valor_total))
        print()
        print('Muito Obrigado!')

    cont = input('''Deseja realizar um novo cálculo ? (S / N)
''').capitalize()