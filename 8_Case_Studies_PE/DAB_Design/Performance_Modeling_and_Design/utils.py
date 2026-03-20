import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_map(df, features):
    """
    Plots a correlation heatmap for the given features in the dataframe.
    Returns the correlation matrix.
    """
    plt.figure(figsize=(10, 8))
    correlation_matrix = df[features].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                square=True, fmt='.3f')
    plt.title('Correlation Map of Input and Output Features')
    plt.tight_layout()
    plt.show()
    return correlation_matrix

def plot_feature_histograms(df, features):
    """
    Plots histograms for each feature in the features list.
    """
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    axes = axes.ravel()

    for i, feature in enumerate(features):
        axes[i].hist(df[feature], bins=30, alpha=0.7, edgecolor='black')
        axes[i].set_title(f'Histogram of {feature}')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel('Frequency')

    # Hide the last subplot if we have less than 8 features
    if len(features) < 8:
        axes[-1].set_visible(False)

    plt.tight_layout()
    plt.show()

def basic_statistical_analysis(df, features, correlation_matrix=None):
    """
    Prints basic data analysis, feature statistics, feature ranges,
    top 5 strongest correlations, and missing value information.
    Optionally accepts a precomputed correlation_matrix.
    """
    print("=== BASIC DATA ANALYSIS ===")
    print(f"Total number of samples: {len(df)}")
    print("\n=== FEATURE STATISTICS ===")
    print(df[features].describe())

    print("\n=== FEATURE RANGES ===")
    for feature in features:
        min_val = df[feature].min()
        max_val = df[feature].max()
        mean_val = df[feature].mean()
        std_val = df[feature].std()
        print(f"{feature}: min={min_val:.3f}, max={max_val:.3f}, mean={mean_val:.3f}, std={std_val:.3f}")

    print("\n=== CORRELATION ANALYSIS ===")
    if correlation_matrix is None:
        correlation_matrix = df[features].corr()
    correlations = correlation_matrix.unstack()
    correlations = correlations[correlations != 1.0]  # Remove self-correlations
    strongest_corr = correlations.abs().sort_values(ascending=False).head(5)
    print("Top 5 strongest correlations:")
    for idx, value in strongest_corr.items():
        print(f"{idx[0]} vs {idx[1]}: {value:.3f}")

    print("\n=== MISSING VALUES ===")
    missing_values = df[features].isnull().sum()
    if missing_values.sum() == 0:
        print("No missing values found in the selected features.")
    else:
        print(missing_values[missing_values > 0])

def plot_and_summarize_pca_results(
    explained_variance_ratio,
    cumulative_variance_ratio,
    X_pca_transformed,
    pca,
    pca_features
):
    """
    Plots PCA results and prints a summary.

    Parameters:
        explained_variance_ratio (array-like): Explained variance ratio for each PC.
        cumulative_variance_ratio (array-like): Cumulative explained variance ratio.
        X_pca_transformed (ndarray): Data transformed by PCA (n_samples, n_components).
        pca (PCA object): Fitted PCA object.
        pca_features (list): List of feature names used in PCA.
    """
    import matplotlib.pyplot as plt
    import numpy as np

    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    # Plot 1: Explained variance ratio
    axes[0, 0].bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, alpha=0.7)
    axes[0, 0].set_xlabel('Principal Component')
    axes[0, 0].set_ylabel('Explained Variance Ratio')
    axes[0, 0].set_title('Explained Variance Ratio by Principal Component')
    axes[0, 0].grid(True, alpha=0.3)

    # Plot 2: Cumulative explained variance
    axes[0, 1].plot(
        range(1, len(cumulative_variance_ratio) + 1),
        cumulative_variance_ratio,
        'bo-',
        linewidth=2,
        markersize=8
    )
    axes[0, 1].axhline(y=0.95, color='r', linestyle='--', alpha=0.7, label='95% Variance')
    axes[0, 1].axhline(y=0.99, color='orange', linestyle='--', alpha=0.7, label='99% Variance')
    axes[0, 1].set_xlabel('Number of Principal Components')
    axes[0, 1].set_ylabel('Cumulative Explained Variance Ratio')
    axes[0, 1].set_title('Cumulative Explained Variance Ratio')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)

    # Plot 3: First two principal components scatter plot
    axes[1, 0].scatter(X_pca_transformed[:, 0], X_pca_transformed[:, 1], alpha=0.6, s=20)
    axes[1, 0].set_xlabel(f'PC1 ({explained_variance_ratio[0]:.3f} variance)')
    axes[1, 0].set_ylabel(f'PC2 ({explained_variance_ratio[1]:.3f} variance)')
    axes[1, 0].set_title('First Two Principal Components')
    axes[1, 0].grid(True, alpha=0.3)

    # Plot 4: Feature loadings for first two principal components
    loadings = pca.components_[:2, :]
    x_pos = np.arange(len(pca_features))
    width = 0.35

    axes[1, 1].bar(x_pos - width/2, loadings[0], width, label='PC1', alpha=0.7)
    axes[1, 1].bar(x_pos + width/2, loadings[1], width, label='PC2', alpha=0.7)
    axes[1, 1].set_xlabel('Features')
    axes[1, 1].set_ylabel('Loading Values')
    axes[1, 1].set_title('Feature Loadings for First Two Principal Components')
    axes[1, 1].set_xticks(x_pos)
    axes[1, 1].set_xticklabels(pca_features, rotation=45)
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Print PCA summary
    print("=== PCA ANALYSIS RESULTS ===")
    print(f"Features used: {pca_features}")
    print(f"\nExplained variance ratio:")
    for i, var in enumerate(explained_variance_ratio):
        print(f"PC{i+1}: {var:.4f} ({var*100:.2f}%)")

    print(f"\nCumulative explained variance:")
    for i, var in enumerate(cumulative_variance_ratio):
        print(f"PC1-PC{i+1}: {var:.4f} ({var*100:.2f}%)")

    print(f"\nNumber of components needed for:")
    print(f"95% variance: {np.argmax(cumulative_variance_ratio >= 0.95) + 1}")
    print(f"99% variance: {np.argmax(cumulative_variance_ratio >= 0.99) + 1}")

    print(f"\nFeature loadings for PC1:")
    for feature, loading in zip(pca_features, pca.components_[0]):
        print(f"{feature}: {loading:.4f}")

    print(f"\nFeature loadings for PC2:")
    for feature, loading in zip(pca_features, pca.components_[1]):
        print(f"{feature}: {loading:.4f}")

def plot_tsne_analysis(
    df_final,
    voltage_levels,
    voltage_color_map,
    input_tsne,
    output_tsne,
    combined_tsne,
    input_features,
    output_features,
    power_levels=None,
    power_color_map=None
):
    """
    Plots t-SNE scatter plots for input, output, and combined features, colored by voltage level
    or by (voltage, power) combination if power_levels and power_color_map are provided.
    Prints summary statistics.

    Parameters:
        df_final (pd.DataFrame): DataFrame containing the data, must have 'Vref' column.
        voltage_levels (iterable): Iterable of voltage levels to plot.
        voltage_color_map (dict): Mapping from voltage level to color.
        input_tsne (np.ndarray): t-SNE transformed input features (n_samples, 2).
        output_tsne (np.ndarray): t-SNE transformed output features (n_samples, 2).
        combined_tsne (np.ndarray): t-SNE transformed combined features (n_samples, 2).
        input_features (list): List of input feature names.
        output_features (list): List of output feature names.
        power_levels (iterable, optional): Iterable of power levels to plot. If None, only voltage is used.
        power_color_map (dict, optional): Mapping from power level to color. Required if power_levels is given.
    """
    import numpy as np
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Helper to determine if we use power-level coloring
    use_power = power_levels is not None and power_color_map is not None

    # 1. t-SNE for Input Features
    if use_power:
        for voltage in voltage_levels:
            for power in power_levels:
                mask = (df_final['Vref'] == voltage) & (df_final['P'] == power)
                if mask.any():
                    color = np.array(voltage_color_map[voltage]) * 0.7 + np.array(power_color_map[power]) * 0.3
                    axes[0].scatter(input_tsne[mask, 0], input_tsne[mask, 1],
                                    c=[color], label=f'Vref={voltage}V, P={power}W', alpha=0.7, s=30)
        axes[0].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    else:
        for voltage in voltage_levels:
            mask = df_final['Vref'] == voltage
            axes[0].scatter(input_tsne[mask, 0], input_tsne[mask, 1],
                            c=[voltage_color_map[voltage]], label=f'Vref={voltage}V', alpha=0.7)
        axes[0].legend()
    axes[0].set_xlabel('t-SNE Component 1')
    axes[0].set_ylabel('t-SNE Component 2')
    axes[0].set_title('t-SNE of Input Features\n(Vref, P, D0, D1, D2)')
    axes[0].grid(True, alpha=0.3)

    # 2. t-SNE for Output Features
    if use_power:
        for voltage in voltage_levels:
            for power in power_levels:
                mask = (df_final['Vref'] == voltage) & (df_final['P'] == power)
                if mask.any():
                    color = np.array(voltage_color_map[voltage]) * 0.7 + np.array(power_color_map[power]) * 0.3
                    axes[1].scatter(output_tsne[mask, 0], output_tsne[mask, 1],
                                    c=[color], label=f'Vref={voltage}V, P={power}W', alpha=0.7, s=30)
        axes[1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    else:
        for voltage in voltage_levels:
            mask = df_final['Vref'] == voltage
            axes[1].scatter(output_tsne[mask, 0], output_tsne[mask, 1],
                            c=[voltage_color_map[voltage]], label=f'Vref={voltage}V', alpha=0.7)
        axes[1].legend()
    axes[1].set_xlabel('t-SNE Component 1')
    axes[1].set_ylabel('t-SNE Component 2')
    axes[1].set_title('t-SNE of Output Features\n(ipk2pk, total_ZVS)')
    axes[1].grid(True, alpha=0.3)

    # 3. t-SNE for Combined Features
    if use_power:
        for voltage in voltage_levels:
            for power in power_levels:
                mask = (df_final['Vref'] == voltage) & (df_final['P'] == power)
                if mask.any():
                    color = np.array(voltage_color_map[voltage]) * 0.7 + np.array(power_color_map[power]) * 0.3
                    axes[2].scatter(combined_tsne[mask, 0], combined_tsne[mask, 1],
                                    c=[color], label=f'Vref={voltage}V, P={power}W', alpha=0.7, s=30)
        axes[2].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    else:
        for voltage in voltage_levels:
            mask = df_final['Vref'] == voltage
            axes[2].scatter(combined_tsne[mask, 0], combined_tsne[mask, 1],
                            c=[voltage_color_map[voltage]], label=f'Vref={voltage}V', alpha=0.7)
        axes[2].legend()
    axes[2].set_xlabel('t-SNE Component 1')
    axes[2].set_ylabel('t-SNE Component 2')
    axes[2].set_title('t-SNE of Combined Features\n(Input + Output)')
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Print summary statistics
    print("\n=== t-SNE ANALYSIS SUMMARY ===")
    print(f"Input features: {input_features}")
    print(f"Output features: {output_features}")
    print(f"Combined features: {input_features + output_features}")
    print(f"Number of samples: {len(df_final)}")
    print(f"Voltage levels found: {sorted(voltage_levels)}")
    if use_power:
        print(f"Power levels found: {sorted(power_levels)}")
        
def plot_and_report_model_performance(
    mse, rmse, r2,
    train_losses, test_losses,
    y_test, y_pred,
    model_NN_regression, X_test_scaled, input_features
):
    """
    Plots and prints model performance, training history, predictions vs actual,
    and feature importance using permutation importance.

    Parameters:
        mse (float): Mean Squared Error
        rmse (float): Root Mean Squared Error
        r2 (float): R^2 Score
        train_losses (list): Training loss per epoch
        test_losses (list): Test loss per epoch
        y_test (array-like): True target values
        y_pred (array-like): Predicted target values
        model_NN_regression (callable): Trained model
        X_test_scaled (ndarray): Scaled test features
        input_features (list): List of feature names
    """
    import torch
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.metrics import r2_score

    print(f"\n=== MODEL PERFORMANCE ===")
    print(f"Mean Squared Error: {mse:.6f}")
    print(f"Root Mean Squared Error: {rmse:.6f}")
    print(f"R² Score: {r2:.6f}")

    # Plot training history
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(train_losses, label='Training Loss')
    plt.plot(test_losses, label='Test Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training History')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Plot predictions vs actual
    plt.subplot(1, 2, 2)
    plt.scatter(y_test, y_pred, alpha=0.6)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual ipk2pk')
    plt.ylabel('Predicted ipk2pk')
    plt.title(f'Predictions vs Actual\nR² = {r2:.4f}')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Feature importance analysis (using permutation importance)
    def permutation_importance(model_NN_regression, X, y, feature_names):
        base_score = r2_score(y, model_NN_regression(torch.FloatTensor(X)).detach().numpy().flatten())
        importance_scores = []
        
        for i in range(X.shape[1]):
            X_permuted = X.copy()
            np.random.shuffle(X_permuted[:, i])
            permuted_score = r2_score(y, model_NN_regression(torch.FloatTensor(X_permuted)).detach().numpy().flatten())
            importance_scores.append(base_score - permuted_score)
        
        return importance_scores

    # Calculate feature importance
    importance_scores = permutation_importance(model_NN_regression, X_test_scaled, y_test, input_features)

    # Plot feature importance
    plt.figure(figsize=(8, 6))
    bars = plt.bar(input_features, importance_scores)
    plt.xlabel('Features')
    plt.ylabel('Importance Score')
    plt.title('Feature Importance (Permutation)')
    plt.xticks(rotation=45)

    # Add value labels on bars
    for bar, score in zip(bars, importance_scores):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001, 
                 f'{score:.4f}', ha='center', va='bottom')

    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    print(f"\n=== FEATURE IMPORTANCE ===")
    for feature, importance in zip(input_features, importance_scores):
        print(f"{feature}: {importance:.6f}")

def plot_stress_mesh_and_contour(D1_original, D2_original, stress_mesh, 
                                 mesh_title='3D Mesh Plot: Current Stress vs D1 and D2\n(P=100, Vref=240)', 
                                 contour_title='2D Contour Plot: Current Stress vs D1 and D2\n(P=100, Vref=240)'):
    """
    Plots a 3D mesh and a 2D contour plot for current stress as a function of D1 and D2.

    Parameters:
        D1_original (np.ndarray): Meshgrid array for D1.
        D2_original (np.ndarray): Meshgrid array for D2.
        stress_mesh (np.ndarray): Meshgrid array for current stress (ipk2pk).
        mesh_title (str): Title for the 3D mesh plot.
        contour_title (str): Title for the 2D contour plot.
    """
    import matplotlib.pyplot as plt

    # Create 3D mesh plot
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot mesh surface
    mesh = ax.plot_surface(D1_original, D2_original, stress_mesh, cmap='viridis', alpha=0.8)
    ax.set_xlabel('D1')
    ax.set_ylabel('D2')
    ax.set_zlabel('Current Stress (ipk2pk)')
    ax.set_title(mesh_title)

    # Set rotation angle for better viewing
    ax.view_init(elev=20, azim=45)

    # Add colorbar
    fig.colorbar(mesh, ax=ax, shrink=0.5, aspect=5)

    plt.tight_layout()
    plt.show()

    # Also create a 2D contour plot for better visualization
    plt.figure(figsize=(10, 8))
    # Change contour lines to a light color (e.g., 'white' or a pale grey)
    contour_2d = plt.contour(D1_original, D2_original, stress_mesh, 20, colors='#eeeeee', alpha=0.9)
    plt.contourf(D1_original, D2_original, stress_mesh, 20, cmap='viridis')
    plt.colorbar(label='Current Stress (ipk2pk)')
    plt.xlabel('D1')
    plt.ylabel('D2')
    plt.title(contour_title)
    plt.grid(True, alpha=0.3)
    plt.show()


def plot_classification_results(
    train_losses,
    test_losses,
    y_test_mapped,
    y_pred_classes,
    model_NN_classification,
    X_test_scaled,
    input_features
):
    """
    Plots training history, confusion matrix, feature importance, and prints classification report for ZVS classification.

    Parameters:
        train_losses (list or np.ndarray): Training loss values per epoch.
        test_losses (list or np.ndarray): Test loss values per epoch.
        y_test_mapped (np.ndarray): True class labels for test set.
        y_pred_classes (np.ndarray): Predicted class labels for test set.
        model_NN_classification (torch.nn.Module): Trained classification model.
        X_test_scaled (np.ndarray): Scaled test input features.
        input_features (list): List of input feature names.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    import torch
    from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
    import seaborn as sns

    # Plot training history
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(train_losses, label='Training Loss')
    plt.plot(test_losses, label='Test Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('ZVS Classification Training History')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Plot confusion matrix
    plt.subplot(1, 2, 2)
    cm = confusion_matrix(y_test_mapped, y_pred_classes)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['ZVS=4', 'ZVS=6', 'ZVS=8'],
                yticklabels=['ZVS=4', 'ZVS=6', 'ZVS=8'])
    plt.xlabel('Predicted ZVS')
    plt.ylabel('Actual ZVS')
    plt.title('Confusion Matrix')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Feature importance analysis for classification
    def classification_permutation_importance(model_NN_classification, X, y, feature_names):
        base_score = accuracy_score(y, torch.argmax(model_NN_classification(torch.FloatTensor(X)), dim=1).numpy())
        importance_scores = []

        for i in range(X.shape[1]):
            X_permuted = X.copy()
            np.random.shuffle(X_permuted[:, i])
            permuted_score = accuracy_score(y, torch.argmax(model_NN_classification(torch.FloatTensor(X_permuted)), dim=1).numpy())
            importance_scores.append(base_score - permuted_score)

        return importance_scores

    # Calculate feature importance for classification
    importance_scores = classification_permutation_importance(
        model_NN_classification, X_test_scaled, y_test_mapped, input_features
    )

    # Plot feature importance
    plt.figure(figsize=(8, 6))
    bars = plt.bar(input_features, importance_scores)
    plt.xlabel('Features')
    plt.ylabel('Importance Score (Accuracy Drop)')
    plt.title('Feature Importance for ZVS Classification')
    plt.xticks(rotation=45)

    # Add value labels on bars
    for bar, score in zip(bars, importance_scores):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001,
                 f'{score:.4f}', ha='center', va='bottom')

    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    print(f"\n=== FEATURE IMPORTANCE FOR ZVS CLASSIFICATION ===")
    for feature, importance in zip(input_features, importance_scores):
        print(f"{feature}: {importance:.6f}")

    # Additional classification report
    print(f"\n=== DETAILED CLASSIFICATION REPORT ===")
    print(classification_report(y_test_mapped, y_pred_classes, target_names=['ZVS=4', 'ZVS=6', 'ZVS=8']))

def plot_2d_zvs_classification(D1_original, D2_original, zvs_mesh, P_fixed, Vref_fixed):
    """
    Plots a 2D classification plot for ZVS conditions using square/rectangle patches (pcolormesh) with less dazzling colors.

    Parameters:
        D1_original (np.ndarray): Array of D1 values.
        D2_original (np.ndarray): Array of D2 values.
        zvs_mesh (np.ndarray): Array of ZVS class labels (0, 1, 2).
        P_fixed (float or str): Fixed power value for the plot title.
        Vref_fixed (float or str): Fixed Vref value for the plot title.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.patches import Patch
    from matplotlib.colors import ListedColormap

    plt.figure(figsize=(10, 8))

    # Define less dazzling colors for different ZVS conditions
    colors = ['#8da0cb', '#dddddd', '#E76F51']  # muted blue, light grey, custom orange/red
    labels = ['ZVS=4', 'ZVS=6', 'ZVS=8']
    cmap = ListedColormap(colors)

    # Create a grid for pcolormesh
    # We'll bin the data into a 2D histogram and plot with pcolormesh
    nbins = 50
    D1_bins = np.linspace(np.min(D1_original), np.max(D1_original), nbins + 1)
    D2_bins = np.linspace(np.min(D2_original), np.max(D2_original), nbins + 1)

    # For each bin, assign the most common ZVS class in that bin
    hist = np.full((nbins, nbins), np.nan)
    for i in range(nbins):
        for j in range(nbins):
            mask = (
                (D1_original >= D1_bins[i]) & (D1_original < D1_bins[i+1]) &
                (D2_original >= D2_bins[j]) & (D2_original < D2_bins[j+1])
            )
            if np.any(mask):
                # Assign the most frequent class in this bin
                vals, counts = np.unique(zvs_mesh[mask], return_counts=True)
                hist[j, i] = vals[np.argmax(counts)]

    # Plot with pcolormesh
    mesh = plt.pcolormesh(
        D1_bins, D2_bins, hist,
        cmap=cmap, shading='auto', vmin=0, vmax=2, alpha=0.7
    )

    # Custom legend using patches
    legend_handles = [Patch(facecolor=colors[i], edgecolor='grey', label=labels[i]) for i in range(3)]
    plt.xlabel('D1')
    plt.ylabel('D2')
    plt.title(f'2D ZVS Classification Plot (Squares): D1 vs D2\n(P={P_fixed}, Vref={Vref_fixed})')
    plt.legend(handles=legend_handles)
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.show()


def plot_xgboost_feature_importance_and_predictions(
    feature_names, feature_importance,
    y_train, y_train_pred, train_r2,
    y_test, y_test_pred, test_r2
):
    """
    Plots XGBoost feature importance and actual vs predicted values for training and test sets.

    Parameters:
        feature_names (list): List of feature names.
        feature_importance (array-like): Importance scores for each feature.
        y_train (array-like): Actual values for the training set.
        y_train_pred (array-like): Predicted values for the training set.
        train_r2 (float): R^2 score for the training set.
        y_test (array-like): Actual values for the test set.
        y_test_pred (array-like): Predicted values for the test set.
        test_r2 (float): R^2 score for the test set.
    """
    import matplotlib.pyplot as plt

    # Plot feature importance
    plt.figure(figsize=(10, 6))
    plt.bar(feature_names, feature_importance)
    plt.title('XGBoost Feature Importance')
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot actual vs predicted
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Training set
    ax1.scatter(y_train, y_train_pred, alpha=0.5)
    ax1.plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'r--', lw=2)
    ax1.set_xlabel('Actual Values')
    ax1.set_ylabel('Predicted Values')
    ax1.set_title(f'Training Set (R² = {train_r2:.4f})')
    ax1.grid(True, alpha=0.3)

    # Test set
    ax2.scatter(y_test, y_test_pred, alpha=0.5)
    ax2.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    ax2.set_xlabel('Actual Values')
    ax2.set_ylabel('Predicted Values')
    ax2.set_title(f'Test Set (R² = {test_r2:.4f})')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

def classification_analysis(
    y_train, y_train_pred, train_accuracy,
    y_test, y_test_pred, test_accuracy,
    xgb_classifier, input_features,
    y_mapped
):
    """
    Performs classification analysis including:
    - Confusion matrices for train and test sets
    - Feature importance plot and printout
    - Detailed classification report
    - Class distribution plots and dataset summary

    Parameters:
        y_train (array-like): True labels for training set.
        y_train_pred (array-like): Predicted labels for training set.
        train_accuracy (float): Accuracy for training set.
        y_test (array-like): True labels for test set.
        y_test_pred (array-like): Predicted labels for test set.
        test_accuracy (float): Accuracy for test set.
        xgb_classifier: Trained XGBoost classifier.
        input_features (list): List of feature names.
        y_mapped (array-like): All mapped labels (for class count).
    """
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    from sklearn.metrics import confusion_matrix, classification_report

    # Plot confusion matrix
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    cm_train = confusion_matrix(y_train, y_train_pred)
    sns.heatmap(cm_train, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['ZVS=4', 'ZVS=6', 'ZVS=8'], 
                yticklabels=['ZVS=4', 'ZVS=6', 'ZVS=8'])
    plt.xlabel('Predicted ZVS')
    plt.ylabel('Actual ZVS')
    plt.title(f'Training Confusion Matrix (Accuracy: {train_accuracy:.4f})')

    plt.subplot(1, 2, 2)
    cm_test = confusion_matrix(y_test, y_test_pred)
    sns.heatmap(cm_test, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['ZVS=4', 'ZVS=6', 'ZVS=8'], 
                yticklabels=['ZVS=4', 'ZVS=6', 'ZVS=8'])
    plt.xlabel('Predicted ZVS')
    plt.ylabel('Actual ZVS')
    plt.title(f'Test Confusion Matrix (Accuracy: {test_accuracy:.4f})')

    plt.tight_layout()
    plt.show()

    # Feature importance analysis
    feature_importance = xgb_classifier.feature_importances_

    # Plot feature importance
    plt.figure(figsize=(10, 6))
    bars = plt.bar(input_features, feature_importance)
    plt.xlabel('Features')
    plt.ylabel('Importance Score')
    plt.title('XGBoost Feature Importance for ZVS Classification')
    plt.xticks(rotation=45)

    # Add value labels on bars
    for bar, importance in zip(bars, feature_importance):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                 f'{importance:.4f}', ha='center', va='bottom')

    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Detailed classification report
    print(f"\n=== DETAILED CLASSIFICATION REPORT ===")
    print(classification_report(y_test, y_test_pred, target_names=['ZVS=4', 'ZVS=6', 'ZVS=8']))

    # Print feature importance scores
    print(f"\n=== FEATURE IMPORTANCE FOR ZVS CLASSIFICATION ===")
    for feature, importance in zip(input_features, feature_importance):
        print(f"{feature}: {importance:.6f}")

    # Additional analysis: Class distribution
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    unique_train, counts_train = np.unique(y_train, return_counts=True)
    plt.bar(['ZVS=4', 'ZVS=6', 'ZVS=8'], counts_train)
    plt.title('Training Set Class Distribution')
    plt.ylabel('Count')

    plt.subplot(1, 3, 2)
    unique_test, counts_test = np.unique(y_test, return_counts=True)
    plt.bar(['ZVS=4', 'ZVS=6', 'ZVS=8'], counts_test)
    plt.title('Test Set Class Distribution')
    plt.ylabel('Count')

    plt.subplot(1, 3, 3)
    plt.bar(['Train', 'Test'], [len(y_train), len(y_test)])
    plt.title('Dataset Split')
    plt.ylabel('Number of Samples')

    plt.tight_layout()
    plt.show()

    print(f"\n=== DATASET SUMMARY ===")
    print(f"Training samples: {len(y_train)}")
    print(f"Test samples: {len(y_test)}")
    print(f"Total samples: {len(y_train) + len(y_test)}")
    print(f"Number of classes: {len(np.unique(y_mapped))}")


def plot_pso_optimization_results(optimizer, best_pos, best_cost):
    """
    Plots the PSO optimization progress and prints the best results.

    Parameters:
    - optimizer: The PSO optimizer object with cost_history and pos_history attributes.
    - best_pos: The best position found (array-like, shape (2,))
    - best_cost: The best objective function value found (float)
    """
    # Plot optimization progress
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(optimizer.cost_history)
    plt.title('PSO Optimization Progress')
    plt.xlabel('Iteration')
    plt.ylabel('Objective Function Value')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.scatter(optimizer.pos_history[-1][:, 0], optimizer.pos_history[-1][:, 1], alpha=0.6)
    plt.scatter(best_pos[0], best_pos[1], color='red', s=100, marker='*', label='Best Solution')
    plt.xlabel('D1')
    plt.ylabel('D2')
    plt.title('Final Particle Positions')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    # Print results
    print(f"\n=== PSO OPTIMIZATION RESULTS ===")
    print(f"Best D1: {best_pos[0]:.4f}")
    print(f"Best D2: {best_pos[1]:.4f}")
    print(f"Best objective value: {best_cost:.4f}")