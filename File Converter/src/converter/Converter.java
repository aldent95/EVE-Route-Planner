package converter;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.regex.Pattern;

import javax.swing.JFileChooser;

public class Converter {
	private String filename1 = "Gates.txt";
	private String filename2 = "Gates2.txt";
	private String sysname = "Systems.txt";
	private String jumpname = "Jumps.txt";
	private String outname = "Stargates.txt";
	private File gates = new File("src/files/" + filename1);
	private File gates2 = new File("src/files/" + filename2);
	private File outfile = new File("src/files/" + outname);
	private File systems = new File("src/files/" + "Systems.txt");
	private File jumps = new File("src/files/" + "Jumps.txt");
	private HashMap<Integer, Gate> gate = new HashMap<Integer, Gate>();
	private ArrayList<Integer> gateIDs = new ArrayList<Integer>();
	private HashMap<Integer, Integer> jump = new HashMap<Integer, Integer>();
	private HashMap<String, Integer> system = new HashMap<String, Integer>();
	private boolean headers = true;

	public static void main(String[] args) {
		new Converter();
	}

	public Converter() {
		read();
	}

	private String stupidfuckingcode(String line) {
		if (line.contains("﻿"))
			return line.replaceAll("﻿", "");
		else
			return line;
	}

	private void read() {
		BufferedReader data1;
		BufferedReader data2;
		String line1 = "temp";
		String line2 = "temp";
		try {
			data1 = new BufferedReader(new FileReader(systems));
			line1 = "temp";
			while (line1 != null) {
				line1 = data1.readLine();
				if (line1 == null)
					break;
				line1 = stupidfuckingcode(line1);
				String[] values = line1.split("\t");
				system.put(values[3], Integer.parseInt(values[2]));
			}
			data1 = new BufferedReader(new FileReader(jumps));
			line1 = "temp";
			while (line1 != null) {
				line1 = data1.readLine();
				if (line1 == null)
					break;
				line1 = stupidfuckingcode(line1);
				String[] values = line1.split("\t");
				jump.put(Integer.parseInt(values[1]),
						Integer.parseInt(values[0]));
			}
			line1 = "temp";
			line2 = "temp";
			data1 = new BufferedReader(new FileReader(gates));
			data2 = new BufferedReader(new FileReader(gates2));
			while (line1 != null && line2 != null) {
				line1 = data1.readLine();
				if (line1 == null)
					break;
				line1 = stupidfuckingcode(line1);
				String[] values1 = line1.split("\t");
				line2 = data2.readLine();
				if (line2 == null)
					break;
				line2 = stupidfuckingcode(line2);
				String[] values2 = line2.split("\t");
				convert1(values1, values2);
			}
			data1.close();
			data2.close();
			convert2();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private void write(String[] towrite, BufferedWriter writer) {
		String sep = "\t";
		try {
			if (headers == false) {
				writer.write("ItemID,x,y,z,start,end\n");
				headers = true;
			}
			writer.append(towrite[0] + sep + towrite[1] + sep + towrite[2]
					+ sep + towrite[3] + sep + towrite[4] + sep + towrite[5]
					+ "\n");
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private void convert1(String[] gates, String[] gates2) {
		String gatename = gates[1].replaceAll("Stargate|[(]|[)]", "");
		if (gatename.startsWith((" ")))
			gatename = gatename.replaceFirst(" ", "");
		Gate g = new Gate(Integer.parseInt(gates[0]),
				Double.parseDouble(gates2[1]), Double.parseDouble(gates2[2]),
				Double.parseDouble(gates2[3]), gatename);
		if (system.get(gatename) != null) {
			g.dest = system.get(gatename);
			gateIDs.add(Integer.parseInt(gates[0]));
			gate.put(Integer.parseInt(gates[0]), g);
		}

	}

	private void convert2() {
		try {
			BufferedWriter writer;
			writer = new BufferedWriter(new OutputStreamWriter(
					new FileOutputStream(outfile), "utf-8"));
			for (Integer i : gateIDs) {
				Gate g = gate.get(i);
				g.system = gate.get(jump.get(g.ID)).dest;
				write(g.toArray(), writer);

			}
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}
}
