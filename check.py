from inference import load_model, get_dataloaders


train_loader, val_loader, test_loader = get_dataloaders(r'data', batch_size=6)
