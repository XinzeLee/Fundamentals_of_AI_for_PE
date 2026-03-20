%% sweep_BuckConverter.m
% Parameter sweep for BuckConverter.slx  (open-loop buck converter)
% -------------------------------------------------------------------------
%  param_1: L (RL.L)         ↳ block parameter on model root
%  param_2: C  (Series RLC Branch1.C)    ↳ inductor inside block mask
%
%  OUTPUT:  'results' still need to be configured
% -------------------------------------------------------------------------

%% 1. Define sweep vectors
L_vec = [50e-6 100e-6 150e-6];          % Ω  (edit as needed)
C_vec  = [100e-6 200e-6 400e-6];      % H  (edit as needed)

%% 2. Pre-allocate results container
nRuns = numel(L_vec) * numel(C_vec);
results = table('Size',[nRuns 3], ...
                'VariableTypes',{'double','double','double'}, ...
                'VariableNames',{'RL','L','Vout_final'});

runID = 0;

%% 3. Load model once
mdl = 'BuckConverter';
load_system(mdl);

%% 4. Create SimulationInput objects + run
for i = 1:numel(L_vec)
    for j = 1:numel(C_vec)
        runID = runID + 1;

        L_val = L_vec(i);
        C_val  = C_vec(j);

        % Build a fresh SimulationInput for each combo
        in = Simulink.SimulationInput(mdl);

        % ---- Set model-level parameter RL ------------
        blkPath = [mdl '/RL'];
        in  = in.setBlockParameter(blkPath, 'Resistance', num2str(L_val));  % workspace or mask param

        % ---- Set inductor L inside 'Series RLC Branch1' block ----
        blkPath = [mdl '/Series RLC Branch1'];
        in  = in.setBlockParameter(blkPath,'Capacitance', num2str(C_val));

        % ---- (Optional) Specify which signals to log ----
        in  = in.setModelParameter('SaveOutput','on', ...
                                   'SignalLogging','on');
        % Assume Vout signal is marked for logging
        % You can also add a Simulink.SimulationData.SignalSpecification here

        % ---- Run simulation ----
        simOut = sim(in);

        % ---- Extract final value of Vout ----
        % Logged as simOut.logsout.get('Vout')
        % 🔧 Option 1: Mark 'Vout' signal for logging manually
        % Open your model BuckConverter.slx.
        % Right-click the signal line for output voltage (e.g., from a sensor or scope input).
        % Select Properties → Check "Log signal data".
        % Name the signal as 'Vout'.
        Vsig   = simOut.get('Vout');     % timeseries

        % ---- Process Vsig later on ----
    end
end

%% 5. Display or export results
% disp(results);
% writetable(results,'sweep_results.csv');   % uncomment to save
