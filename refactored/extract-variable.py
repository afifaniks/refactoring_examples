def renderBanner(self):
    is_mac = self.platform.toUpperCase().indexOf("MAC") > -1
    is_ie = self.browser.toUpperCase().indexOf("IE") > -1
    is_initialized = self.wasInitialized()
    is_resized = self.resize > 0
    
    if is_mac and is_ie and is_initialized and is_resized:
        pass
