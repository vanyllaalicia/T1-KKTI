import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        System.out.println("=== Array ===");

        Mahasiswa[] kelas = new Mahasiswa[3];

        kelas[0] = new Mahasiswa("Nadine", "F1D02410129");
        kelas[1] = new Mahasiswa("Potaa", "F1D02410130");
        kelas[2] = new Mahasiswa("Alicia", "F1D02410131");

        for (Mahasiswa m : kelas) {
            m.tampilkanInfo();
            System.out.println();
        }

        System.out.println("=== ArrayList ===");

        ArrayList<Mahasiswa> daftar = new ArrayList<>();

        daftar.add(new Mahasiswa("Fely", "F1D02410112"));
        daftar.add(new Mahasiswa("Inas", "F1D02410133"));
        daftar.add(new Mahasiswa("Putri", "F1D02410134"));

        System.out.println("Jumlah mahasiswa: " + daftar.size());

        System.out.println("\nData mahasiswa:");
        for (Mahasiswa m : daftar) {
            m.tampilkanInfo();
            System.out.println();
        }

        daftar.remove(1);

        System.out.println("Setelah menghapus data kedua:");
        for (Mahasiswa m : daftar) {
            m.tampilkanInfo();
            System.out.println();
        }
    }
}