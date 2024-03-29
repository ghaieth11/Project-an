function simulate_epidemic()

    % Paramètres de la simulation
    num_individuals = 100;  % Nombre total d'individus
    num_infected = 1;       % Nombre initial d'individus infectés
    simulation_time = 100;  % Durée de la simulation

    % Paramètres du système différentiel
    beta = 0.3;   % Taux de transmission
    alpha = 0.1;  % Taux de récupération
    gamma = 0.05; % Taux de transition de I à T
    eta = 0.02;   % Taux de transition de T à R
    delta = 0.1;  % Facteur pour le modèle de délai

    % Conditions initiales du système différentiel
    S = 0.99;
    I = 0.01;
    T = 0;
    R = 0;

    % Créer la figure et définir les axes
    figure;
    axis([0 10 0 10]);
    xlabel('Position X');
    ylabel('Position Y');
    title('Simulation d''épidémie');

    % Initialiser les positions et les états des individus
    positions = 10 * rand(num_individuals, 2);  % Positions aléatoires
    states = zeros(num_individuals, 1);          % 0: Sain, 1: Infecté, 2: Exposé, 3: Récupéré, 4: Décédé
    states(1:num_infected) = 1;                 % Définir les premiers individus comme infectés

    % Couleurs pour les différents états
    colors = ['b'; 'r'; 'm'; 'g'; 'k'];  % Bleu: Sain, Rouge: Infecté, Magenta: Exposé, Vert: Récupéré, Noir: Décédé

    % Dessiner les cercles pour chaque individu
    circles = cell(num_individuals, 1);
    for i = 1:num_individuals
        circles{i} = rectangle('Position', [positions(i, 1)-0.25, positions(i, 2)-0.25, 0.5, 0.5], ...
            'Curvature', [1, 1], 'FaceColor', colors(states(i)+1, :));
    end

    % Boucle de simulation
    for t = 1:simulation_time
        % Mettre à jour les états des individus en fonction des valeurs du système différentiel
        dS = -beta * S * I;
        dI = beta * S * I - (alpha + gamma) * I;
        dT = gamma * I - eta * T;
        dR = eta * T;
        
        % Mise à jour des populations
        S = S + dS;
        I = I + dI;
        T = T + dT;
        R = R + dR;
        
        % Mettre à jour les états des individus en fonction des nouvelles valeurs du système différentiel
        for i = 1:num_individuals
            % Déplacer les individus aléatoirement
            positions(i, :) = positions(i, :) + randn(1, 2) * 0.1;

            % Vérifier les collisions avec les bords de la zone
            positions(i, 1) = max(min(positions(i, 1), 10), 0);
            positions(i, 2) = max(min(positions(i, 2), 10), 0);
            
            % Définir l'état en fonction des valeurs des populations
            if rand < S
                states(i) = 0;  % Sain
            elseif rand < S + I
                states(i) = 1;  % Infecté
            elseif rand < S + I + T
                states(i) = 2;  % Exposé
            elseif rand < S + I + T + R
                states(i) = 3;  % Récupéré
            else
                states(i) = 4;  % Décédé
            end

            % Mettre à jour la couleur et la position du cercle en fonction de l'état
            set(circles{i}, 'Position', [positions(i, 1)-0.25, positions(i, 2)-0.25, 0.5, 0.5], ...
                'FaceColor', colors(states(i)+1, :));
        end

        % Mettre à jour l'affichage
        drawnow;
        pause(0.01);  % Pause pour ralentir la simulation
    end
end

