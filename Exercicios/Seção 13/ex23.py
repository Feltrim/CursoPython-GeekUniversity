with open("emp.txt", "w") as arquivo:
    for i in range(5):
        profissao = input(f"Profissão do funcionário {i+1}: ")
        tempo_servico = input(f"Tempo de serviço do funcionário {i+1}: ")
        arquivo.write(f"{profissao},{tempo_servico}\n")
