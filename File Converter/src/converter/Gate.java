package converter;

public class Gate {
	public int ID;
	public double x;
	public double y;
	public double z;
	public int system;
	public int dest;
	public String destname;
	public Gate(int ID, double d, double e, double f, String name){
		this.ID = ID;
		this.x = d;
		this.y = e;
		this.z = f;
		destname = name;
	}
	public String[] toArray(){
		String[] array = new String[6];
		array[0] = Integer.toString(ID);
		array[1] = Double.toString(x);
		array[2] = Double.toString(y);
		array[3] = Double.toString(z);
		array[4] = Integer.toString(system);
		array[5] = Integer.toString(dest);
		return array;
				
	}
}
