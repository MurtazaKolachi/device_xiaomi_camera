package miui.os;

/** Minimal MIUI build API required by the stock MiuiScanner application. */
public final class Build {
    public static final boolean IS_ALPHA_BUILD = false;
    public static final boolean IS_DEVELOPMENT_VERSION = false;
    public static final boolean IS_STABLE_VERSION = true;
    public static final boolean IS_INTERNATIONAL_BUILD = true;
    public static final boolean IS_MITWO = false;
    public static final boolean IS_MI2A = false;

    private Build() {}

    public static boolean checkRegion(String region) {
        return false;
    }
}
