clear;

% Método de Síntese Direta

s = tf('s');

tfAquecedorAquecimento = tf([0.5], [51 1]); % AA
tfAquecedorResfriamento = tf([0.5], [105 1]); % AR
tfVentiladorResfriamento = tf([-0.0322], [30 1]); %VR

tauControladorAA = 51*0.8; 

GControladorAA = (1/tfAquecedorAquecimento)*(1/(tauControladorAA*s));

% Feedforward

ganhoFF = tfVentiladorResfriamento/tfAquecedorAquecimento;